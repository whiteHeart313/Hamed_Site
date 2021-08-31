# Generated by Django 3.2.6 on 2021-08-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_sold_products_year_month_day_solds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='buy_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='sell_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=19, null=True),
        ),
    ]