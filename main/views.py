from django.shortcuts import render
from django.http import HttpResponse
from .my_forms import EmployeeForm
from .models import Employee, Rank, Post
from datetime import date

table_names = {'property':'имущество','promotions':'поощрения', 'relatives':'члены семьи', 'auto':'личные автомобили','vaccination':'вакцинация','education':'образование'}
 
def index(request):	
    employees = Employee.objects.all()
    
    return render(request, "index.html", {'data':employees})

def person(request):
    employees = Employee.objects.all()
    employee_id = request.POST.get('employee_id')
    direction = request.POST.get('direction', None)
    if direction == '+':
        employee_id = str(int(employee_id) + 1)
    elif direction == '-':
        employee_id = str(int(employee_id) - 1)

    if int(employee_id) < 1:
        employee_id = str(len(employees))
    elif int(employee_id) > len(employees):
        employee_id = '1'

    employee = Employee.objects.get(id=employee_id)
    return render(request, "person.html", context={'employee':employee})

def add_person(request):
    employee_form = EmployeeForm()
    
    if request.method == 'GET': return render(request, 'add_person.html', {"form": employee_form})
    elif request.method == 'POST':
        data = request.POST
        
        employee = Employee.objects.create(name = data['name'], 
                                           second_name = data['second_name'],
                                           third_name = data['third_name'],
                                           rank = Rank.objects.get(id=int(data['rank'])),
                                           post = Post.objects.get(id=int(data['post'])),
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
    

def information(request):
    employee_id = request.POST.get('employee_id')
    employee = Employee.objects.get(id=employee_id)
    table = request.POST.get('table')
    return render(request, "information_table.html", context={'employee':employee_id, 'table_name':f'{employee.second_name} {employee.name} {employee.third_name} - {table_names[table]}'})