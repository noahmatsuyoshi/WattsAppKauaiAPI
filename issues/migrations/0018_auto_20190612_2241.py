# Generated by Django 2.2 on 2019-06-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0017_auto_20190612_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='issueImage'),
        ),
    ]