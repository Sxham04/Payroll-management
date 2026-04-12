from django.contrib import admin
from .models import Employee, Attendance, SalaryRecord

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(SalaryRecord)