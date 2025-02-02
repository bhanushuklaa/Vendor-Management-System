# Generated by Django 5.0.1 on 2024-05-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_historicalperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='average_respose_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fullFillMent_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
