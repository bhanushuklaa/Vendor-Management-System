# Generated by Django 5.0.1 on 2024-05-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_vendor_average_respose_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]