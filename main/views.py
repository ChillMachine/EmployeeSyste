from django.shortcuts import render
from django.http import HttpResponse
from .my_forms import *
from .models import *
from datetime import date

table_names = {'Property':'имущество',
               'Promotions':'поощрения', 
               'Relatives':'члены семьи', 
               'Auto':'личные автомобили',
               'Vaccination':'вакцинация',
               'Education':'образование',
               'Training':'переподготовка',
               'Weapons':'закрепленное оружие',
               'Driver_license':'категории водительского удостоверения',
               'Clothing_sizes':'размеры одежды'}
tables = {  'Property':Property,
            'Promotions': Promotions, 
            'Relatives': Relatives, 
            'Auto': Auto,
            'Vaccination': Vaccination,
            'Education': Education,
            'Training': Training,
            'Weapons': Weapons,
            'Driver_license': Driver_license,
            'Clothing_sizes': Clothing_sizes}


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
    data = request.POST
    employee_id = data['employee_id']
    employee = Employee.objects.get(id=employee_id)
    if data.get('filling', 'False') == 'True':
        if data['table_name'] == 'Property': PropertyForm(data).save()
        elif data['table_name'] == 'Promotions': PromotionsForm(data).save()
        elif data['table_name'] == 'Relatives': RelativesForm(data).save()
        elif data['table_name'] == 'Auto': AutoForm(data).save()
        elif data['table_name'] == 'Vaccination': VaccinationForm(data).save()
        elif data['table_name'] == 'Education': EducationForm(data).save()
        elif data['table_name'] == 'Training': TrainingForm(data).save()
        elif data['table_name'] == 'Weapons': WeaponsForm(data).save()
        
    table_name = data['table_name']
    table = tables[table_name].objects.filter(employee_id=employee_id)
    property_form, promotions_form, relatives_form = PropertyForm(), PromotionsForm(), RelativesForm()
    auto_form, vaccination_form, education_form = AutoForm(), VaccinationForm(), EducationForm()
    training_form, weapons_form = TrainingForm(), WeaponsForm()

    context = {'table': table ,
               'table_name': table_name,
               'employee_id':employee_id,
               'title':f'{employee.second_name} {employee.name} {employee.third_name} - {table_names[table_name]}',
               'property_form': property_form,
               'promotions_form': promotions_form,
               'relatives_form': relatives_form,
               'auto_form': auto_form,
               'vaccination_form': vaccination_form,
               'education_form': education_form,
               'training_form': training_form,
               'weapons_form': weapons_form}
    
    return render(request, "information_table.html", context)
