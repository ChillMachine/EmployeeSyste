from django.shortcuts import render
from .my_forms import *
from .models import *


tables = { 'Property':Property, 'Promotions': Promotions, 'Relatives': Relatives, 
           'Auto': Auto, 'Vaccination': Vaccination, 'Education': Education, 
           'Training': Training, 'Weapons': Weapons}
table_names = {'Property':'имущество', 'Promotions':'поощрения', 'Relatives':'члены семьи', 
               'Auto':'личные автомобили', 'Vaccination':'вакцинация', 'Education':'образование',
               'Training':'переподготовка', 'Weapons':'закрепленное оружие'}
my_forms = {'property_form': PropertyForm, 'promotions_form': PromotionsForm, 'relatives_form': RelativesForm, 
            'auto_form': AutoForm, 'vaccination_form': VaccinationForm, 'education_form': EducationForm,
            'training_form': TrainingForm, 'weapons_form': WeaponsForm}

def index(request):
    if request.method == 'POST':
        data = request.POST
        if 'button' in data and data['button'] == 'del':
            employee_to_del = Employee.objects.get(id=data['employee_id'])
            vacansy_data = {'post_num':employee_to_del.post_num,
                            'post':employee_to_del.post,
                            'group_num':employee_to_del.group_num,
                            'rank':employee_to_del.post.rank}

            employee_to_del.delete()
            Employee.objects.create(**vacansy_data)

    employees = Employee.objects.all()
    context = {'data':employees}
    return render(request, "index.html", context)

def person(request):
    if request.method == 'POST':
        data = request.POST
        employees_count = len(Employee.objects.all())
        direction = data.get('direction', None)
        post_num = Employee.objects.get(id=data['employee_id']).post_num

        if direction == '+':
            post_num = str(int(post_num) + 1)
        elif direction == '-':
            post_num = str(int(post_num) - 1)

        if int(post_num) < 1:
            post_num = str(employees_count)
        elif int(post_num) > employees_count:
            post_num = '1'

        if 'edit_button' in data:   
            if data['edit_button'] == 'edited':
                employee = Employee.objects.get(id = data['employee_id'])
                employee.second_name = data['second_name']
                employee.name = data['name']
                employee.third_name = data['third_name']
                employee.rank = Rank.objects.get(id=data['rank'])
                employee.post = Post.objects.get(id=data['post'])
                employee.group_num = data['group_num']
                employee.appointment_order_num = data['order_num']
                employee.appointment_order_date = data['order_date']
                employee.b_day = data['b_day']
                employee.place_of_bd = data['place_of_bd']
                employee.phone_number = data['phone_number']
                employee.family_status = data['family_status']
                employee.personal_num = data['personal_num']
                employee.address = data['address']
                employee.save()

        employee = Employee.objects.get(id=Employee.objects.get(post_num=post_num).id)

        

        context = {'employee':employee}
        if 'msg' in data:
            context['msg'] = data['msg']
        return render(request, "person.html", context)
    else:
        employees = Employee.objects.all()
        context = {'data':employees}
        return render(request, "index.html", context) 


def information(request):
    if request.method == 'POST':
        data = request.POST
        employee_id = request.POST['employee_id']
        employee = Employee.objects.get(id=employee_id)
        if data.get('filling', 'False') == 'True':
            form = my_forms[f"{data['table_name'].lower()}_form"](data)
            if form.is_valid():
                form.save()

        table_name = data['table_name']
        table = tables[table_name].objects.filter(employee_id=employee_id)
        context = {'table': table ,
                'table_name': table_name,
                'employee_id':employee_id,
                'title':f'{employee.second_name} {employee.name} {employee.third_name} - {table_names[table_name]}'} | my_forms
        if 'row_del' in data:
            row_to_del = tables[data['table_name']].objects.get(id=data['row_del'])
            row_to_del.delete()

        return render(request, "information_table.html", context)
    else:
        employees = Employee.objects.all()
        context = {'data':employees}
        return render(request, "index.html", context) 

def edit(request):
    if request.method == 'POST':
        
        data = request.POST
        post_num = Employee.objects.get(id=data['employee_id']).post_num
        employee = Employee.objects.get(id=Employee.objects.get(post_num=post_num).id)
        form = EmployeeForm(initial={'group_num': employee.group_num, 'post':employee.post, 'rank': employee.rank, 'family_status':employee.family_status})
        context = {'employee':employee, 'form':form}
        

            
        return render(request, "edit.html", context)

    else:
        employees = Employee.objects.all()
        context = {'data':employees}
        return render(request, "index.html", context)