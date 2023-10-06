from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    rank = models.IntegerField()
    post = models.IntegerField()
    b_day = models.DateField()
    personal_num = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=20)
    group = models.CharField(max_length=10)
    family_status = models.CharField(max_length=10)
    place_of_bd = models.CharField(max_length=20)
    appointment_order_num = models.CharField(max_length=10)
    appointment_order_date = models.DateField()