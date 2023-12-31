# Generated by Django 2.2.3 on 2019-09-13 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_in', models.IntegerField()),
                ('cash_out', models.IntegerField()),
                ('description_cash_in', models.CharField(max_length=300)),
                ('description_cash_out', models.CharField(max_length=300)),
                ('date_filed', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'cash_records',
            },
        ),
    ]
