# Generated by Django 4.1.7 on 2023-10-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_training_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapons',
            name='description',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='weapons',
            name='rec_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
