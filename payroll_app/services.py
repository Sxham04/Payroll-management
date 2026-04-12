from .models import Attendance, SalaryRecord

def calculate_monthly_salary(employee, month, year):
    # 1. Count Attendance
    days_present = Attendance.objects.filter(
        employee=employee, 
        date__month=month, 
        date__year=year, 
        is_present=True
    ).count()

    # 2. Basic Math (Assuming 22 working days per month)
    daily_rate = employee.base_salary / 22
    gross_pay = daily_rate * days_present

    # 3. Tax Logic (Objective: Tax Deduction)
    tax_rate = 0.15 if gross_pay > 5000 else 0.05
    tax_amount = gross_pay * tax_rate
    net_pay = gross_pay - tax_amount

    # 4. Save to Database
    salary_record = SalaryRecord.objects.create(
        employee=employee,
        month=month,
        year=year,
        gross_pay=gross_pay,
        tax_deducted=tax_amount,
        net_pay=net_pay
    )
    return salary_record