# Generated by Django 4.2.5 on 2023-10-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_employee_second_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='second_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]