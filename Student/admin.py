from django.contrib import admin
from .models import RandomChallan
from .models import FeeRecords
from .models import CashRecords

# Register your models here.


@admin.register(FeeRecords)
class FeeRecordsAdmin(admin.ModelAdmin):
   	list_display = ('challan_no', 'student_name')

@admin.register(RandomChallan)
class RandomChallanAdmin(admin.ModelAdmin):
   	list_display = ('challan_no', 'student_name')

admin.site.register(CashRecords)


