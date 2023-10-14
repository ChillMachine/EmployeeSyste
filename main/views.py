from django.shortcuts import render
from django.http import HttpResponse
from .my_forms import EmployeeForm
from .models import Employee, Rank, Post, Auto, Promotions, Property, Relatives, Training, Weapons, Vaccination, Education, Driver_license, Clothing_sizes
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
        if data['table_name'] == 'Property':
            prop = Property.objects.create(name = data['name'],
                                           inv_num = data['inv_num'],
                                           date_of_rec = data['date_of_rec'],
                                           description = data['description'],
                                           status = data['status'],
                                           employee_id = Employee.objects.get(id=int(employee_id)))
            prop.save()
        elif data['table_name'] == 'Promotions':
            promotion = Promotions.objects.create(promotion_type=data['promotion_type'],
                                                  rights=data['rights'],
                                                  date=data['date'],
                                                  order_num=data['order_num'],
                                                  description=data['description'],
                                                  employee_id=Employee.objects.get(id=int(employee_id)))
            promotion.save()  
        elif data['table_name'] == 'Relatives':
            second_name, name, third_name = data['FIO'].split()
            relative = Relatives.objects.create(name=name,
                                                second_name=second_name,
                                                third_name=third_name,
                                                relation_degree=data['relation_degree'],
                                                phone_number=data['phone_number'],
                                                employee_id=Employee.objects.get(id=int(employee_id)))
            relative.save()
        elif data['table_name'] == 'Auto':
            auto = Auto.objects.create(model=data['model'],
                                       gos_num=data['gos_num'],
                                       employee_id=Employee.objects.get(id=int(employee_id)))
            auto.save()
        elif data['table_name'] == 'Vaccination':
            vaccine = Vaccination.objects.create(vaccine_name=data['vaccine_name'],
                                                 date=data['date'],
                                                 description=data['description'],
                                                 employee_id=Employee.objects.get(id=int(employee_id)))
            vaccine.save()
        elif data['table_name'] == 'Education':
            education = Education.objects.create(grade=data['grade'],
                                                 institution=data['institution'],
                                                 date_of_graduate=data['date_of_graduate'],
                                                 speciality=data['speciality'],
                                                 description=data['description'],
                                                 employee_id=Employee.objects.get(id=int(employee_id)))
            education.save()
        elif data['table_name'] == 'Training':
            training = Training.objects.create(thread_code=data['thread_code'],
                                               institution=data['institution'],
                                               start_date=data['start_date'],
                                               duratin=data['duratin'],
                                               description=data['description'],
                                               employee_id=Employee.objects.get(id=int(employee_id)))
            training.save()
        elif data['table_name'] == 'Weapons':
            weapon = Weapons.objects.create(weapon_name=data['weapon_name'],
                                            count=data['count'],
                                            weapon_num=data['weapon_num'],
                                            rec_date=data['rec_date'],
                                            description=data['description'],
                                            status=data['status'],
                                            employee_id=Employee.objects.get(id=int(employee_id)))
            weapon.save()
        elif data['table_name'] == 'Driver_license':
            pass
        elif data['table_name'] == 'Clothing_sizes':
            pass
        
    table_name = data['table_name']
    table = tables[table_name].objects.filter(employee_id=employee_id)
    return render(request, "information_table.html", context={'table': table , 
                                                              'table_name': table_name, 
                                                              'employee_id':employee_id,
                                                              'title':f'{employee.second_name} {employee.name} {employee.third_name} - {table_names[table_name]}'})
