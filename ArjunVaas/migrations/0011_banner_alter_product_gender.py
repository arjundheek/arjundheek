# Generated by Django 4.1.7 on 2023-03-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArjunVaas', '0010_alter_tryon_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/uploads/banners')),
                ('href', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('man', 'Man'), ('women', 'Women'), ('boy', 'Boy'), ('girl', 'Girl'), ('babyboy', 'Baby Boy'), ('babygirl', 'Baby Girl')], default='', max_length=15),
        ),
    ]
