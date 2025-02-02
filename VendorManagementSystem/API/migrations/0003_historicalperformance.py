# Generated by Django 5.0.1 on 2024-05-02 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_purchaseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_respose_time', models.FloatField()),
                ('fullfillment_rate', models.FloatField()),
                ('Vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.vendor')),
            ],
        ),
    ]
