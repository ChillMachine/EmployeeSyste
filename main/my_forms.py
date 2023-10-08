from django import forms
from .models import Rank, Post

ranks = [(rank.id, rank.rank_name) for rank in Rank.objects.all()]
posts = [(post.id, post.post_name) for post in Post.objects.all()]

class EmployeeForm(forms.Form):
    name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    third_name = forms.CharField(label='Отчество')
    rank = forms.ChoiceField(choices=ranks, label='Звание')
    post = forms.ChoiceField(choices=posts, label='Должность')

    # rank = forms.IntegerField(label='Звание')
    # post = forms.IntegerField(label='Должность')
    group = forms.CharField(label='Группа')
    appointment_order_num = forms.CharField(label='Приказ о назначении на должность')
    appointment_order_date = forms.DateField(label='Дата приказа', widget=forms.SelectDateWidget)
    b_day = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget)
    phone_number = forms.CharField(label='Номер телефона')
    family_status = forms.CharField(label='Семейное положение')
    place_of_bd = forms.CharField(label='Место рождения')
    personal_num = forms.CharField(label='Личный номер')
    address = forms.CharField(label='Адрес места жительства')
    