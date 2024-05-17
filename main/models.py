from django.db import models
from datetime import date

family_statuses = [('холост', 'холост'),('женат', 'женат'),('в разводе', 'в разводе')]
groups = [('-','-'),('Группа 1','Группа 1'),('Группа 2','Группа 2'),('Группа 3','Группа 3'),('Группа 4','Группа 4'),('Группа 5','Группа 5')]

class Rank(models.Model):
    rank_name = models.CharField(max_length=20, unique=True)
    salary = models.CharField(max_length=10)
    
    def __str__(self):
        return self.rank_name

class Post(models.Model):
    post_name = models.CharField(max_length=20, unique=True)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    salary = models.CharField(max_length=10)

    def __str__(self):
        return self.post_name

class Employee(models.Model):
    post_num = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, blank=True, null=True, default='Вакант')
    second_name = models.CharField(max_length=20, blank=True, null=True, default='')
    third_name = models.CharField(max_length=20, blank=True, null=True, default='') 
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    b_day = models.DateField(blank=True, null=True)
    personal_num = models.CharField(max_length=4, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True, default='')
    address = models.CharField(max_length=20, blank=True, null=True, default='')
    group_num = models.CharField(max_length=10, choices=groups)
    family_status = models.CharField(max_length=10, choices=family_statuses, blank=True, null=True)
    place_of_bd = models.CharField(max_length=20, blank=True, null=True, default='')
    appointment_order_num = models.CharField(max_length=10, blank=True, null=True, default='')
    appointment_order_date = models.DateField(blank=True, null=True)
    class Meta:
        ordering = ['post_num']

class Auto(models.Model):
    model = models.CharField(max_length=20)
    gos_num = models.CharField(max_length=10)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Promotions(models.Model):
    promotion_type = models.CharField(max_length=20)
    rights = models.CharField(max_length=20)
    date_of_rec = models.DateField()
    order_num = models.CharField(max_length=10, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True, null=True)

class Property(models.Model):
    name = models.CharField(max_length=20)
    inv_num = models.CharField(max_length=20, default='-', blank=True)
    date_of_rec = models.DateField()
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, default='Выдано')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Relatives(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    relation_degree = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12, default='-', blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Training(models.Model):
    thread_code = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    start_date = models.DateField()
    duratin = models.CharField(max_length=10)
    description = models.CharField(max_length=50, default='-', blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=20)
    count = models.IntegerField(default=1, blank=True)
    weapon_num = models.CharField(max_length=20)
    date_of_rec = models.DateField()
    description = models.CharField(max_length=50, default='-', blank=True, null=True)
    status = models.CharField(max_length=20, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Vaccination(models.Model):
    vaccine_name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=50, blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Education(models.Model):
    grade = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    date_of_graduate = models.DateField()
    speciality = models.CharField(max_length=20, default='-')
    description = models.CharField(max_length=50, blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)