# Generated by Django 4.2.5 on 2023-09-26 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]
