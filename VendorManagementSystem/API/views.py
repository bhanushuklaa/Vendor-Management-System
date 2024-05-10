from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from API.models import Vendor, PurchaseOrder, HistoricalPerformance
from API.serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    HistoricalPerformanceSerializer,
)
from rest_framework.decorators import api_view
from django.db.models import Count, Avg
from datetime import timedelta
from rest_framework.response import Response


# Create your views here.
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor_code = serializer.validated_data.get("vendor_code")
            if Vendor.objects.filter(vendor_code=vendor_code).exists():
                return Response(
                    {"error": "Vendor code must be unique"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["get"])
    # def HistoricalPerformance(self, request, pk=None):
    #     vendor = Vendor.objects.get(pk=pk)
    #     perform = HistoricalPerformance.objects.filter(vendor=vendor)
    #     perform_serializer = HistoricalPerformanceSerializer(
    #         perform, many=True, context={"request": request}
    #     )
    #     return Response(perform_serializer.data)
    @api_view(["GET"])
    def get_vendor_performance(request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)
        calculate_performance_metrics(vendor)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    @api_view(["POST"])
    def acknowledge_purchase_order(request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=404)

        # Update acknowledgment date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Recalculate vendor's average response time
        calculate_performance_metrics(purchase_order.vendor)

        return Response(
            {"success": "Purchase order acknowledged successfully"}, status=200
        )


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

    def calculate_performance_metrics(vendor):
        # On-Time Delivery Rate
        completed_pos = vendor.purchase_orders.filter(status="completed")
        on_time_deliveries = completed_pos.filter(
            delivery_date__lte=models.F("delivery_date")
        ).count()
        total_completed_pos = completed_pos.count()
        vendor.on_time_delivery_rate = (
            (on_time_deliveries / total_completed_pos) * 100
            if total_completed_pos > 0
            else 0.0
        )

        # Quality Rating Average
        completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
        vendor.quality_rating_avg = (
            completed_pos_with_rating.aggregate(avg_rating=Avg("quality_rating"))[
                "avg_rating"
            ]
            or 0.0
        )

        # Average Response Time
        acknowledgment_times = (
            completed_pos.filter(acknowledgment_date__isnull=False)
            .annotate(
                response_time=models.F("acknowledgment_date") - models.F("issue_date")
            )
            .aggregate(avg_response_time=Avg("response_time"))["avg_response_time"]
        )
        vendor.average_response_time = (
            acknowledgment_times.total_seconds() / acknowledgment_times.count()
            if acknowledgment_times
            else 0.0
        )

        # Fulfilment Rate
        successful_pos = completed_pos.exclude(status="canceled")
        vendor.fulfillment_rate = (
            (successful_pos.count() / vendor.purchase_orders.count()) * 100
            if vendor.purchase_orders.count() > 0
            else 0.0
        )

        vendor.save()
