# Generated by Django 4.1.7 on 2023-03-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0012_banner_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='page',
            field=models.CharField(blank=True, choices=[('brand', 'Brand'), ('categories', 'Categories'), ('products', 'Products'), ('tryons', 'Tryons')], default='', max_length=50),
        ),
    ]