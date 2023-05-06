# Generated by Django 4.1.6 on 2023-05-04 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample', '0015_alter_signup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
