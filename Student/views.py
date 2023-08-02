from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Fee, Year, Month, Cash, CashRecords, FeeRecords, FeeChallan, RandomChallan, MonthName
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def add_student(request):
	if (request.method == "POST"):
		my_students = Student.objects.all()
		exist_stud = False
		for stud in my_students:
			if stud.roll_no == int(request.POST['roll_no']):
				exist_stud = True

		if exist_stud == False:
			temp = Student(roll_no = request.POST['roll_no'], name = request.POST['student_name'], father_name = request.POST['father_name'], contact_no = request.POST['contact_no'], class_no = request.POST['class'], section = request.POST['section'], address = request.POST['address'], student_type = request.POST['student_type'])
			temp.save()
			fee = Fee(status = False, amount = 0)
			fee.save()
			now = timezone.now()
			total_months = 13 - now.month
			year = Year(current_year = now.year, total_paid_this_year = 0, total_balance_this_year = fee.amount*total_months)
			year.save()
			month = Month(january = 0, february = 0, march = 0, april = 0, may = 0, june = 0, july = 0, august = 0, september = 0, october = 0, november = 0, december = 0)
			month.save()
			messages.success(request, f'Student With Roll No { temp.roll_no } & Name { temp.name } Added Successfully. Set Student Fee First')
			return redirect('show_student')
		else:
			messages.warning(request, f'Student With Same Roll No Already Exists')

	return render(request, 'add-student.html')

@login_required
def show_student(request):
	month_check()
	my_student = Student.objects.all()
	my_fee = Fee.objects.all()

	now = timezone.now()
	total_months = 13 - now.month
	months = Month.objects.all()

	year = Year.objects.all()

	if year.count() >= 1:
		if year[0].current_year < now.year:
			new_year = Year.objects.all()
			for var in months:
				var.january = 0
				var.february = 0
				var.march = 0
				var.april = 0
				var.may = 0
				var.june = 0
				var.july = 0
				var.august = 0
				var.september = 0
				var.october = 0
				var.november = 0
				var.december = 0
				var.save()
			for var in new_year:
				var.current_year += 1
				var.total_balance_this_year = my_fee[my_fee.count()-(my_fee.count()-var.id)].amount*total_months
				var.total_paid_this_year = months[my_fee.count()-(my_fee.count()-var.id)].january+months[my_fee.count()-(my_fee.count()-var.id)].february+months[my_fee.count()-(my_fee.count()-var.id)].march+months[my_fee.count()-(my_fee.count()-var.id)].april+months[my_fee.count()-(my_fee.count()-var.id)].may+months[my_fee.count()-(my_fee.count()-var.id)].june+months[my_fee.count()-(my_fee.count()-var.id)].july+months[my_fee.count()-(my_fee.count()-var.id)].august+months[my_fee.count()-(my_fee.count()-var.id)].september+months[my_fee.count()-(my_fee.count()-var.id)].october+months[my_fee.count()-(my_fee.count()-var.id)].november+months[my_fee.count()-(my_fee.count()-var.id)].december
				var.save()
			for x in Fee.objects.all():
				x.status = False
				x.save()

	return render(request, 'show-student.html', {'temp': my_student, 'my_fee': my_fee})


def manage_fee(request, id):
	temp = Student.objects.get(id = id)
	fee = Fee.objects.get(id = id)
	year = Year.objects.get(id = id)
	month = Month.objects.get(id = id)
	now  = timezone.now()
	current_month = now.strftime("%B")
	fee_paid = Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	fee_balance = fee.amount - Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	if fee_balance < 0:
		fee_balance = 0
	return render(request, 'manage-fee.html', {'var': temp, 'fee': fee, 'year': year, 'month': month, 'my': current_month, 'my_fee': fee_paid, 'fee_bal': fee_balance})


def pay_fee(request):
	temp = Fee.objects.get(id = int(request.POST['id']))
	current_month = request.POST['month']
	now  = timezone.now()
	my_month = now.strftime("%B")
	month = Month.objects.get(id = int(request.POST['id']))

	if int(request.POST['fee']) > 0:

		if current_month == "January":
			month.january += int(request.POST['fee'])
			if month.january >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "February":
			month.february += int(request.POST['fee'])
			if month.february >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "March":
			month.march += int(request.POST['fee'])
			if month.march >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "April":
			month.april = int(request.POST['fee'])
			if month.april >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "May":
			month.may += int(request.POST['fee'])
			if month.may >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "June":
			month.june += int(request.POST['fee'])
			if month.june >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "July":
			month.july += int(request.POST['fee'])
			if month.july >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "August":
			month.august += int(request.POST['fee'])
			if month.august >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "September":
			month.september += int(request.POST['fee'])
			if month.september >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "October":
			month.october += int(request.POST['fee'])
			if month.october >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "November":
			month.november += int(request.POST['fee'])
			if month.november >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		elif current_month == "December":
			month.december += int(request.POST['fee'])
			if month.december >= temp.amount:
				temp.status = True
			else:
				temp.status = False

		temp.save()
		month.save()
		year = Year.objects.get(id = int(request.POST['id']))
		year.total_paid_this_year += int(request.POST['fee'])
		year.total_balance_this_year -= int(request.POST['fee'])
		year.save()
		cash = Cash.objects.get(id=1)
		cash.total_in += int(request.POST['fee'])
		cash.save()
		student = Student.objects.get(id = int(request.POST['id']))

		new_entry = CashRecords(cash_in = int(request.POST['fee']), cash_out = 0, description_cash_in = f'Roll No {student.roll_no}, Name {student.name}, Paid Fee For Month {current_month}', description_cash_out = 'None', date_filed = datetime.datetime.now())
		new_entry.save()

		today = str(datetime.datetime.now())
		today = today.replace('-', '')
		today = today.replace(' ', '')
		today = today.replace(':', '')
		today = today.replace('.', '')
		today = today[-6:]
		random_num = today

		my_record = FeeRecords(challan_no = random_num, student_roll_no = student.roll_no, student_name = student.name, fee_month = current_month, paid_amount = int(request.POST['fee']), date_filed = datetime.datetime.now())
		my_record.save()

		challan_list = FeeChallan.objects.all()
		if challan_list.count() == 0:
			new_record = FeeChallan(challan_no = random_num, roll_no = student.roll_no)
			new_record.save()
		else:
			for var in challan_list:
				if var.roll_no == student.roll_no:
					var.challan_no = random_num
					var.save()
					break
				elif var.id == challan_list.count():
					new_record = FeeChallan(challan_no = random_num, roll_no = student.roll_no)
					new_record.save()

		my_objects_m = MonthName.objects.all()
		if my_objects_m.count() == 0:
			new_obj_m = MonthName(s_name = "None")
			new_obj_m.save()
		else:
			new_obj_m = MonthName.objects.get(id = 1)
			new_obj_m.s_name = request.POST['month']
			new_obj_m.save()

		messages.success(request, f'Fee Updated Successfully, Month: {current_month}, Roll No: {student.roll_no}, Challan Form # {random_num} Generated')
	else:
		messages.warning(request, f'Please Enter A Valid Fee Amount')
	return redirect(manage_fee, request.POST['id'])


def challan_form(request, id):
	temp = Student.objects.get(id = id)
	fee = Fee.objects.get(id = id)
	years = Year.objects.get(id = id)
	month = Month.objects.get(id = id)
	now  = timezone.now()
	current_month = now.strftime("%B")
	current_year = now.year
	fee_paid = Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	fee_balance = fee.amount - Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	if fee_balance < 0:
		fee_balance = 0
	if (fee.status == True):
		stat = "Paid"
	else:
		stat = "Pending"

	challan_list = FeeChallan.objects.all()
	challan_no = 0
	for var in challan_list:
		if var.roll_no == temp.roll_no:
			challan_no = var.challan_no

	my_new = MonthName.objects.get(id = 1)


	return render(request, 'challan-form.html', {'temp': temp, 'fee': fee, 'years': years, 'month': month, 'my': current_month, 'year': current_year, 'my_fee': fee_paid, 'fee_bal': fee_balance, 'status': stat, 'challan_no': challan_no, 'new_month': my_new})

@login_required
def change_fee(request):
	students_list = Student.objects.all()
	fee_list = Fee.objects.all()
	return render(request, 'change-fee.html', {'students_list': students_list, 'fee_list': fee_list})


def update_fee(request, id):
	selected_student = Student.objects.get(id = id)
	selected_fee = Fee.objects.get(id = id)
	return render(request, 'update-fee.html', {'selected_student': selected_student, 'selected_fee': selected_fee})


def save_fee_amount(request):
	if request.method == 'POST':
		selected_fee = Fee.objects.get(id = int(request.POST['id']))
		selected_fee.amount = request.POST['fee']
		selected_fee.save()

		now = timezone.now()
		current_month = now.month
		total_months_applicable = 13 - current_month
		new_fee_annual_applicable = int(total_months_applicable) * int(selected_fee.amount)

		year = Year.objects.get(id = int(request.POST['id']))

		amount_minused = year.total_balance_this_year - (int(request.POST['current_fee']) * total_months_applicable)
		year.total_balance_this_year = new_fee_annual_applicable + amount_minused

		year.save()
		if int(selected_fee.amount) > int(request.POST['current_fee']):
			selected_fee.status = False
			selected_fee.save()
		else:
			selected_fee.status = True
			selected_fee.save()

		messages.success(request, f'Fee Amount Successfully Updated')
		return redirect(update_fee, selected_fee.id)

@login_required
def struck_off(request):
	students_list = Student.objects.all()
	fee_list = Fee.objects.all()
	return render(request, 'struck-off.html', {'students_list': students_list, 'fee_list': fee_list})


def struck_off_confirm(request, id):
	selected_student = Student.objects.get(id = id)
	return render(request, 'struck-off-confirm.html', {'selected_student': selected_student})

def do_struck_off(request):
	if request.method == 'POST':
		if request.POST['struck_off'] == 'Yes':
			selected_student = Student.objects.get(id = int(request.POST['id']))
			selected_year = Year.objects.get(id = int(request.POST['id']))
			selected_fee = Fee.objects.get(id = int(request.POST['id']))
			selected_month = Month.objects.get(id = int(request.POST['id']))
			messages.success(request, f'Student {selected_student.name} Strucked Off Successfully')
			selected_student.delete()
			selected_year.delete()
			selected_fee.delete()
			selected_month.delete()
		else:
			messages.warning(request, f'Struck off operation has been canceled')
	return redirect(struck_off)

def month_check():
	now = timezone.now()
	date = now.day
	month = now.month
	if date == 1:
		fee_list = Fee.objects.all()
		current_month = now.strftime("%B")
		selected_month = Month.objects.values_list(current_month.lower(), flat = True).all()

		enumerate_object = enumerate(selected_month)

		for var in fee_list:
			iteration = next(enumerate_object)
			index, item = iteration
			if var.amount > item:
				fee_list[index].status = False
				fee_list[index].save()

@login_required
def cash_record(request):
	cash_list = Cash.objects.all()
	if cash_list:
		current_cash = Cash.objects.get(id=1)
		months_list = Month.objects.all()

		return render(request, 'cash-record.html', {'cash_list': current_cash})
	return render(request, 'cash-record.html')


def proceed_cash_in(request):
	if request.method == 'POST':
		cash_list = Cash.objects.get(id = 1)
		if request.POST['proceed_cash_in'] == 'Yes':
			cash_list.total_in += int(request.POST['cash_entered'])
			cash_list.save()
			new_entry = CashRecords(cash_in = int(request.POST['cash_entered']), cash_out = 0, description_cash_in = request.POST['description'], description_cash_out = 'None', date_filed = datetime.datetime.now())
			new_entry.save()
			messages.success(request, f'Cashed In Successfully')
		else:
			messages.warning(request, f'Please Enter Valid Cash Amount For Cash In')
	return redirect(cash_record)


def proceed_cash_out(request):
	if request.method == 'POST':
		cash_list = Cash.objects.get(id = 1)
		if int(request.POST['cash_entered']) <= cash_list.total_in and request.POST['proceed_cash_out'] == 'Yes':
			cash_list.total_in -= int(request.POST['cash_entered'])
			cash_list.total_out += int(request.POST['cash_entered'])
			cash_list.save()
			new_entry = CashRecords(cash_in = 0, cash_out = int(request.POST['cash_entered']), description_cash_in = 'None', description_cash_out = request.POST['description'], date_filed = datetime.datetime.now())
			new_entry.save()
			messages.success(request, f'Cashed Out Successfully')
		else:
			messages.warning(request, f'Please Enter Valid Cash Amount For Cash Out')
	return redirect(cash_record)


def start_session(request):
	counter = Cash.objects.all()
	count = counter.count()
	if count == 0:
		cash = Cash(total_in = 0, total_out = 0)
		cash.save()

		current_cash = Cash.objects.get(id=1)
		months_list = Month.objects.all()
		total = []
		for var in months_list:
			total.append(var.january+var.february+var.march+var.april+var.may+var.june+var.july+var.august+var.september+var.october+var.november+var.december)

		for var in total:
			current_cash.total_in += var
		current_cash.save()
		messages.success(request, f'Session Started Successfully')
	else:
		messages.warning(request, f'Session Already Started')
	return redirect(cash_record)


def saved_records(request):
	records_list = CashRecords.objects.all()
	return render(request, 'saved-records.html', {'records_list': records_list})


def saved_records_out(request):
	records_list = CashRecords.objects.all()
	return render(request, 'saved-records-out.html', {'records_list': records_list})


def fee_history(request):
	records_list = FeeRecords.objects.all()
	return render(request, 'fee-history.html', {'records_list': records_list})


def generate_challan(request):
	return render(request, 'generate-challan.html')


def saved_random_challans(request):
	records_list = RandomChallan.objects.all()
	return render(request, 'saved-random-challans.html', {'records_list': records_list})

def validate_record(request):
	if request.method == 'POST':
		my_student = Student.objects.all()
		count = 0
		if my_student.count() > 0:
			for var in my_student:
				count+=1
				if var.roll_no == int(request.POST['roll_no_entered']):
					current_student = var
					messages.success(request, f'Student Found Successfully')
					return render(request, 'generate-challan.html', {'current_student': current_student})
				elif count == my_student.count():
					messages.warning(request, f'Sorry, Student Did Not Found')
					return redirect(generate_challan)
		else:
			messages.warning(request, f'Sorry, Student Did Not Found')
			return redirect(generate_challan)


def generate_random_challan(request):
	if request.method == 'POST':
		if request.POST['id']:
			temp = Student.objects.get(id = int(request.POST['id']))

			today = str(datetime.datetime.now())
			today = today.replace('-', '')
			today = today.replace(' ', '')
			today = today.replace(':', '')
			today = today.replace('.', '')
			today = today[-6:]
			random_num = today

			new_entry = RandomChallan(challan_no = random_num, student_name = temp.name, roll_no = temp.roll_no, fee_description = request.POST['description'], date_filed = datetime.datetime.now(), paid_amount = int(request.POST['fee']))
			new_entry.save()
			cash = Cash.objects.get(id = 1)
			cash.total_in += new_entry.paid_amount
			cash.save()
			return render(request, 'random-challan.html', {'temp': temp, 'challan': new_entry})
		else:
			messages.warning(request, f'Select Student First & Then Click On Generate Form')
			return redirect(generate_challan)



def save_information(request, id):
	temp = Student.objects.get(id = id)
	fee = Fee.objects.get(id = id)
	year = Year.objects.get(id = id)
	month = Month.objects.get(id = id)
	now  = timezone.now()
	current_month = now.strftime("%B")
	fee_paid = Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	fee_balance = fee.amount - Month.objects.values_list(current_month.lower(), flat = True).get(id = id)
	if fee_balance < 0:
		fee_balance = 0
	return render(request, 'save-information.html', {'var': temp, 'fee': fee, 'year': year, 'month': month, 'my': current_month, 'my_fee': fee_paid, 'fee_bal': fee_balance})
