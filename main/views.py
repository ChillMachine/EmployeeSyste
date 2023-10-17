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
my_forms = {'Property': PropertyForm, 
                     'Promotions': PromotionsForm, 
                     'Relatives': RelativesForm, 
                     'Auto': AutoForm, 
                     'Vaccination': VaccinationForm, 
                     'Education': EducationForm,
                     'Training': TrainingForm,
                     'Weapons': WeaponsForm}


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
    context = {'employee':employee}
    try:
        sizes = Clothing_sizes.objects.get(employee_id=employee_id)
        context['sizes'] = sizes 
    except:
        pass
    try:
        driver_license = Driver_license.objects.get(employee_id=employee_id)
        context['driver_license'] = driver_license
    except:
        pass

    return render(request, "person.html", context)

def add_person(request):
    employee_form = EmployeeForm()
    
    if request.method == 'GET': return render(request, 'add_person.html', {"form": employee_form})
    elif request.method == 'POST':
        data = request.POST
        Employee.objects.create(data).save()
        return render(request, 'add_person.html', {'text':'Сотрудник успешно добавлен', 'form':employee_form})
    else:
        return render(request, "index.html", {'text':'Error'})
    

def information(request):
    data = request.POST
    employee_id = request.POST['employee_id']
    employee = Employee.objects.get(id=employee_id)
    if data.get('filling', 'False') == 'True':
        form = my_forms[data['table_name']](data)
        
        if form.is_valid():
            form.save()

    table_name = data['table_name']
    table = tables[table_name].objects.filter(employee_id=employee_id)
    property_form, promotions_form, relatives_form, auto_form, vaccination_form, education_form, training_form, weapons_form = PropertyForm(), PromotionsForm(), RelativesForm(), AutoForm(), VaccinationForm(), EducationForm(), TrainingForm(), WeaponsForm()

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
