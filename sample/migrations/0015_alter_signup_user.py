# Generated by Django 4.1.6 on 2023-05-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0014_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
