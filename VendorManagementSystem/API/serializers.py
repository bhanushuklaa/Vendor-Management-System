from rest_framework import serializers
from API.models import Vendor, PurchaseOrder, HistoricalPerformance

# Creating Serializers


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class HistoricalPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
