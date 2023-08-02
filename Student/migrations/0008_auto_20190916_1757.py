# Generated by Django 2.2.3 on 2019-09-16 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_auto_20190914_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'month_name',
            },
        ),
        migrations.AlterField(
            model_name='randomchallan',
            name='date_filed',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 16, 17, 57, 25, 347135)),
        ),
    ]
