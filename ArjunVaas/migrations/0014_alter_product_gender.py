# Generated by Django 4.1.7 on 2023-05-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0013_alter_banner_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('boy', 'Boy'), ('girl', 'Girl'), ('babyboy', 'Baby Boy'), ('babygirl', 'Baby Girl')], default='', max_length=15),
        ),
    ]
