# Generated by Django 4.2.5 on 2023-11-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
