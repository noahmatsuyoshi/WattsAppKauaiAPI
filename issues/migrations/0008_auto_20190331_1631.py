# Generated by Django 2.1.7 on 2019-03-31 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20190331_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='posterEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]