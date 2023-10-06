from django.shortcuts import render
from django.http import HttpResponse
from .my_forms import EmployeeForm
from .models import Employee
from datetime import date
 
def index(request):	
    employees = Employee.objects.all()
    
    return render(request, "index.html", {'data':employees})

# def person(request):
#     id = request.POST.get('id', '0')
#     data = {'id': id}
#     if id == '0':
#         return render(request, "index.html", {'text':'Пользователь не найден'})
#     else:
#         return render(request, "person.html", context=data)
    

def add_person(request):
    employee_form = EmployeeForm()
    
    if request.method == 'GET': return render(request, 'add_person.html', {"form": employee_form})
    elif request.method == 'POST':
        data = request.POST
        
        employee = Employee.objects.create(name = data['name'], 
                                           second_name = data['second_name'],
                                           third_name = data['third_name'],
                                           rank = data['rank'],
                                           post = data['post'],
                                           b_day = date(int(data['b_day_year']), int(data['b_day_month']), int(data['b_day_day'])),
                                           personal_num = data['personal_num'],
                                           phone_number = data['phone_number'],
                                           address = data['address'],
                                           group = data['group'],
                                           family_status = data['family_status'],
                                           place_of_bd = data['place_of_bd'],
                                           appointment_order_num = data['appointment_order_num'],
                                           appointment_order_date = date(int(data['appointment_order_date_year']), int(data['appointment_order_date_month']), int(data['appointment_order_date_day'])))
        employee.save()
        return render(request, 'add_person.html', {'text':'Сотрудник успешно добавлен', 'form':employee_form})
    else:
        return render(request, "index.html", {'text':'Error'})
    

 