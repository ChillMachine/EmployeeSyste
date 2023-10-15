from django import forms
from django.forms import ModelForm
from .models import *

ranks = [(rank.id, rank.rank_name) for rank in Rank.objects.all()]
posts = [(post.id, post.post_name) for post in Post.objects.all()]
groups = [(x, f'Группа №{x}') for x in range(1,6)]

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = "__all__"

class PromotionsForm(ModelForm):
    class Meta:
        model = Promotions
        fields = "__all__"       

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class RelativesForm(ModelForm):
    class Meta:
        model = Relatives
        fields = "__all__"

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = "__all__"

class WeaponsForm(ModelForm):
    class Meta:
        model = Weapons
        fields = "__all__"

class VaccinationForm(ModelForm):
    class Meta:
        model = Vaccination
        fields = "__all__"

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = "__all__"

# class Education(models.Model):
#     grade = models.CharField(max_length=20)
#     institution = models.CharField(max_length=20)
#     date_of_graduate = models.DateField()
#     speciality = models.CharField(max_length=20, default='-')
#     description = models.CharField(max_length=50)
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

# class Driver_license(models.Model):
#     A = models.BooleanField()
#     B = models.BooleanField()
#     BE = models.BooleanField()
#     C = models.BooleanField()
#     CE = models.BooleanField()
#     D = models.BooleanField()
#     DE = models.BooleanField()
#     employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)

# class Clothing_sizes(models.Model):
#     head_size = models.CharField(max_length=10)
#     shoes_size = models.CharField(max_length=10)
#     cloth_size = models.CharField(max_length=10)
#     employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)