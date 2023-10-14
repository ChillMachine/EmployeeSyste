from django.db import models
from datetime import date

class Rank(models.Model):
    rank_name = models.CharField(max_length=20)
    salary = models.CharField(max_length=10)

class Post(models.Model):
    post_name = models.CharField(max_length=20)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    salary = models.CharField(max_length=10)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    b_day = models.DateField()
    personal_num = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=20)
    group_num = models.CharField(max_length=10)
    family_status = models.CharField(max_length=10)
    place_of_bd = models.CharField(max_length=20)
    appointment_order_num = models.CharField(max_length=10)
    appointment_order_date = models.DateField()

class Auto(models.Model):
    model = models.CharField(max_length=20)
    gos_num = models.CharField(max_length=10)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

# class Scedule(models.Model):

class Promotions(models.Model):
    promotion_type = models.CharField(max_length=20)
    rights = models.CharField(max_length=20)
    date = models.DateField()
    order_num = models.CharField(max_length=10, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='-')

class Property(models.Model):
    name = models.CharField(max_length=20)
    inv_num = models.CharField(max_length=20)
    date_of_rec = models.DateField()
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Relatives(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    relation_degree = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Training(models.Model):
    thread_code = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    start_date = models.DateField()
    duratin = models.CharField(max_length=10)
    description = models.CharField(max_length=50, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=20)
    count = models.IntegerField()
    weapon_num = models.CharField(max_length=20)
    rec_date = models.DateField()
    description = models.CharField(max_length=50, default='-')
    status = models.CharField(max_length=20, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Vaccination(models.Model):
    vaccine_name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=50)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Education(models.Model):
    grade = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    date_of_graduate = models.DateField()
    speciality = models.CharField(max_length=20, default='-')
    description = models.CharField(max_length=50)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Driver_license(models.Model):
    A = models.BooleanField()
    B = models.BooleanField()
    BE = models.BooleanField()
    C = models.BooleanField()
    CE = models.BooleanField()
    D = models.BooleanField()
    DE = models.BooleanField()
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)

class Clothing_sizes(models.Model):
    head_size = models.CharField(max_length=10)
    shoes_size = models.CharField(max_length=10)
    cloth_size = models.CharField(max_length=10)
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)

