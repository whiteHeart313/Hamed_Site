# Generated by Django 3.2.6 on 2021-08-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_dialyincome'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialyincome',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True),
        ),
    ]
