# Generated by Django 4.1.7 on 2023-05-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0018_alter_product_try_on_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='try_on_image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='try_on_image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='try_on_main_image',
        ),
    ]
