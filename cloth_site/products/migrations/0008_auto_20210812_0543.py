# Generated by Django 3.1.5 on 2021-08-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210812_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
