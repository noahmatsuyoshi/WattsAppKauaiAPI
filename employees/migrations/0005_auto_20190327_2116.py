# Generated by Django 2.1.7 on 2019-03-28 04:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
