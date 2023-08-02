from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_student, name = "show_student"),
    path('add/', views.add_student, name = "add_student"),
    path('show/', views.show_student, name = "show_student"),
    path('manage_fee/<int:id>', views.manage_fee, name = "manage_fee"),
    path('pay_fee/', views.pay_fee, name = "pay_fee"),
    path('challan_form/<int:id>', views.challan_form, name = "challan_form"),
    path('change_fee/', views.change_fee, name = "change_fee"),
    path('update_fee/<int:id>', views.update_fee, name = "update_fee"),
    path('save_fee_amount/', views.save_fee_amount, name = "save_fee_amount"),
    path('struck_off/', views.struck_off, name = "struck_off"),
    path('struck_off_confirm/<int:id>', views.struck_off_confirm, name = "struck_off_confirm"),
    path('do_struck_off/', views.do_struck_off, name = "do_struck_off"),
    path('cash_record/', views.cash_record, name = "cash_record"),
    path('proceed_cash_out/', views.proceed_cash_out, name = "proceed_cash_out"),
    path('proceed_cash_in/', views.proceed_cash_in, name = "proceed_cash_in"),
    path('start_session/', views.start_session, name = "start_session"),
    path('saved_records/', views.saved_records, name = "saved_records"),
    path('saved_records_out/', views.saved_records_out, name = "saved_records_out"),
    path('fee_history/', views.fee_history, name = "fee_history"),
    path('generate_challan/', views.generate_challan, name = "generate_challan"),
    path('saved_random_challans/', views.saved_random_challans, name = "saved_random_challans"),
    path('validate_record/', views.validate_record, name = "validate_record"),
    path('generate_random_challan/', views.generate_random_challan, name = "generate_random_challan"),
    path('save_information/<int:id>', views.save_information, name = "save_information"),
]