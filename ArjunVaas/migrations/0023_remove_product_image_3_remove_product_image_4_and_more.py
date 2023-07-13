# Generated by Django 4.1.7 on 2023-05-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0022_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_5',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_try_on_image1_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_try_on_image2_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_try_on_main_image_enabled',
            field=models.BooleanField(default=False),
        ),
    ]