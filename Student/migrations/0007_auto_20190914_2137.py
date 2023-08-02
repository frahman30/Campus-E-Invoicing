# Generated by Django 2.2.3 on 2019-09-14 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_auto_20190914_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomchallan',
            name='paid_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='challan_no',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='date_filed',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 21, 37, 55, 999126)),
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='fee_description',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='roll_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='student_name',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
