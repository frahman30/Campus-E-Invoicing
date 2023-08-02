from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
	roll_no = models.IntegerField()
	name = models.CharField(max_length=30)
	father_name = models.CharField(max_length=30)
	contact_no = models.CharField(max_length=15)
	class_no = models.CharField(max_length=50)
	section = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	student_type = models.CharField(max_length=30)
	class Meta:
		db_table = "student"

class Fee(models.Model):
	status = models.BooleanField()
	amount = models.IntegerField()
	class Meta:
		db_table = "fee"

class Year(models.Model):
	current_year = models.IntegerField()
	total_paid_this_year = models.IntegerField()
	total_balance_this_year = models.IntegerField()
	class Meta:
		db_table = "year"

class Month(models.Model):
	january = models.IntegerField()
	february = models.IntegerField()
	march = models.IntegerField()
	april = models.IntegerField()
	may = models.IntegerField()
	june = models.IntegerField()
	july = models.IntegerField()
	august = models.IntegerField()
	september = models.IntegerField()
	october = models.IntegerField()
	november = models.IntegerField()
	december = models.IntegerField()
	class Meta:
		db_table = "month"

class Cash(models.Model):
	total_in = models.IntegerField()
	total_out = models.IntegerField()
	class Meta:
		db_table = "cash"

class CashRecords(models.Model):
	cash_in = models.IntegerField()
	cash_out = models.IntegerField()
	description_cash_in = models.CharField(max_length=300)
	description_cash_out = models.CharField(max_length=300)
	date_filed = models.DateTimeField()
	class Meta:
		db_table = "cash_records"

class FeeRecords(models.Model):
	challan_no = models.CharField(max_length=10)
	student_roll_no = models.IntegerField()
	student_name = models.CharField(max_length=30)
	fee_month = models.CharField(max_length=30)
	paid_amount = models.IntegerField()
	date_filed = models.DateTimeField()
	class Meta:
		db_table = "fee_records"

class FeeChallan(models.Model):
	challan_no = models.CharField(max_length=10)
	roll_no = models.IntegerField()
	class Meta:
		db_table = "fee_challan"

class RandomChallan(models.Model):
	challan_no = models.CharField(max_length=10, default='None')
	student_name = models.CharField(max_length=30, default='None')
	roll_no = models.IntegerField(default=0)
	fee_description = models.CharField(max_length=300, default='None')
	date_filed = models.DateTimeField()
	paid_amount = models.IntegerField(default=0)
	class Meta:
		db_table = "random_challan"

class MonthName(models.Model):
	s_name = models.CharField(max_length = 30)
	class Meta:
		db_table = "month_name"