from django.contrib import admin
from API.models import Vendor, PurchaseOrder, HistoricalPerformance

# Register your models here.
# resiteration class of Vendor models


class VendorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact_details",
        "address",
        "average_respose_time",
        "fullfillment_rate",
        "quality_rating_avg",
        "on_time_delivery_rate",
    )


admin.site.register(Vendor, VendorAdmin)


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("po_number", "order_date", "items", "quantity", "status")


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "Vendor",
        "date",
        "average_respose_time",
        "fullfillment_rate",
        "quality_rating_avg",
        "on_time_delivery_rate",
    )


admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
