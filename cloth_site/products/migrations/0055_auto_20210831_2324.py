# Generated by Django 3.2.6 on 2021-08-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0054_books_stat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dialyincome',
            old_name='profit',
            new_name='book_profit',
        ),
        migrations.AddField(
            model_name='dialyincome',
            name='stat_profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True),
        ),
    ]