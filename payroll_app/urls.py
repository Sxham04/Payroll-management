from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('salaries/', views.salary_list, name='salary_list'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('generate/<int:emp_id>/', views.generate_salary, name='generate_salary'),
    path('payslip/<int:pk>/', views.payslip_detail, name='payslip_detail'),
    path('employees/', views.manage_employees, name='manage_employees'),
]