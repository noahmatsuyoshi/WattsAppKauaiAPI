# Generated by Django 2.2 on 2019-05-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20190511_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]