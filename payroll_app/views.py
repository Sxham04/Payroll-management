from django.shortcuts import render, redirect, get_object_or_404
from .models import SalaryRecord, Employee, Attendance
from datetime import date


def salary_list(request):
    salaries = SalaryRecord.objects.all()
    return render(request, 'payroll_app/salary_list.html', {'salaries': salaries})

def mark_attendance(request):
    employees = Employee.objects.all()
    
    if request.method == "POST":
        for emp in employees:
            # Get the status for each specific employee based on their ID
            status_val = request.POST.get(f'status_{emp.id}')
            is_present = (status_val == 'Present')
            
            Attendance.objects.create(
                employee=emp,
                date=date.today(),
                is_present=is_present
            )
        return redirect('salary_list')
        
    return render(request, 'payroll_app/attendance_form.html', {
        'employees': employees,
        'date': date.today()
    })

def generate_salary(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    # Count present days for current month
    days_present = Attendance.objects.filter(employee=employee, is_present=True).count()
    
    # Logic: Basic math
    daily_rate = float(employee.base_salary) / 30
    gross_pay = daily_rate * days_present
    
    # Tax Logic: 10% if gross > 5000, else 5%
    tax_rate = 0.10 if gross_pay > 5000 else 0.05
    tax_amount = gross_pay * tax_rate
    net_pay = gross_pay - tax_amount

    SalaryRecord.objects.create(
        employee=employee,
        month=date.today().month,
        year=date.today().year,
        gross_pay=gross_pay,
        tax_deducted=tax_amount,
        net_pay=net_pay
    )
    return redirect('salary_list')

def payslip_detail(request, pk):
    record = get_object_or_404(SalaryRecord, pk=pk)
    return render(request, 'payroll_app/payslip.html', {'record': record})

def dashboard(request):
    return render(request, 'payroll_app/dashboard.html')