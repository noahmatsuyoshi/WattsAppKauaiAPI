# Generated by Django 2.1.5 on 2019-04-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_auto_20190331_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='posterPhone',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
