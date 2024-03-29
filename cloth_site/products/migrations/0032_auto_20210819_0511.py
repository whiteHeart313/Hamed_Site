# Generated by Django 3.2.6 on 2021-08-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_bills_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='discounts',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='the_rest_of_money',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='user_paied',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True),
        ),
    ]
