# Generated by Django 2.2 on 2019-06-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0018_auto_20190612_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
