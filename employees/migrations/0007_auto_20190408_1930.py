# Generated by Django 2.1.5 on 2019-04-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20190331_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='passwordChange',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
