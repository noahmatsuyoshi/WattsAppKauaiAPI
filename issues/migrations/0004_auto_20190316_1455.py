# Generated by Django 2.1.7 on 2019-03-16 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0003_issue_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='email',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='name',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='phone',
        ),
        migrations.AddField(
            model_name='issue',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]