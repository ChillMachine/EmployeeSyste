from django import forms
from .models import Rank, Post

ranks = [(rank.id, rank.rank_name) for rank in Rank.objects.all()]
posts = [(post.id, post.post_name) for post in Post.objects.all()]
groups = [(x, f'Группа №{x}') for x in range(1,6)]

class EmployeeForm(forms.Form):
    second_name = forms.CharField(label='Фамилия')
    name = forms.CharField(label='Имя')
    third_name = forms.CharField(label='Отчество')
    rank = forms.ChoiceField(choices=ranks, label='Звание')
    post = forms.ChoiceField(choices=posts, label='Должность')
    group = forms.ChoiceField(choices=groups, label='Группа')
    appointment_order_num = forms.CharField(label='Приказ о назначении на должность')
    appointment_order_date = forms.DateField(label='Дата приказа', widget=forms.SelectDateWidget)
    b_day = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget)
    phone_number = forms.RegexField('^(?:\+7|8)[0-9]{10}$',label='Номер телефона')
    family_status = forms.CharField(label='Семейное положение')
    place_of_bd = forms.CharField(label='Место рождения')
    personal_num = forms.CharField(label='Личный номер')
    address = forms.CharField(label='Адрес места жительства')
    