# Generated by Django 4.1.7 on 2023-05-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0016_rename_try_on_enabled_product_try_on_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='try_on_image3',
        ),
        migrations.AddField(
            model_name='product',
            name='try_on_main_image',
            field=models.BooleanField(default=False),
        ),
    ]
