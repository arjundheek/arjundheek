# Generated by Django 4.1.7 on 2023-05-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0019_remove_product_try_on_image1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='try_on_image1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='try_on_image2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='try_on_main_image',
            field=models.BooleanField(default=True),
        ),
    ]
