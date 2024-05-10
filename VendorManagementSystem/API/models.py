from django.db import models

# Create your models here.


# Vendor models
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, blank=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_respose_time = models.FloatField(default=0.0)
    fullfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + "" + self.contact_details


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=12)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(auto_now_add=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(default=0.0)
    issue_date = models.DateTimeField(default=0.0)
    acknowledgment_date = models.DateTimeField(default=0.0)


class HistoricalPerformance(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_respose_time = models.FloatField(default=0.0)
    fullfillment_rate = models.FloatField(default=0.0)
