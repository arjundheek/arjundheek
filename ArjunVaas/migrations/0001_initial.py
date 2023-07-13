# Generated by Django 4.1.7 on 2023-03-13 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('logo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArjunVaas.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='')),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(upload_to='')),
                ('image_3', models.ImageField(upload_to='')),
                ('image_4', models.ImageField(upload_to='')),
                ('image_5', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArjunVaas.category')),
            ],
        ),
    ]
