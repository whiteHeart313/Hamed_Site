# Generated by Django 3.2.6 on 2021-08-22 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
    ]
