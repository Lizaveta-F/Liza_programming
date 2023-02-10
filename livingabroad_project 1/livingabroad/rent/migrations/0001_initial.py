# Generated by Django 4.1 on 2023-02-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='England_rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(verbose_name='link')),
                ('link', models.URLField(verbose_name='link')),
                ('price', models.CharField(max_length=30, verbose_name='price')),
                ('description', models.CharField(max_length=250, verbose_name='description')),
                ('location', models.CharField(max_length=250, verbose_name='location')),
                ('rooms_flat', models.CharField(max_length=200, verbose_name='rooms_flat')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Northireland_rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(verbose_name='link')),
                ('link', models.URLField(verbose_name='link')),
                ('price', models.CharField(max_length=30, verbose_name='price')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('rooms_flat', models.CharField(max_length=150, verbose_name='rooms_flat')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Scotland_rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(verbose_name='link')),
                ('link', models.URLField(verbose_name='link')),
                ('price', models.CharField(max_length=30, verbose_name='price')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('rooms_flat', models.CharField(max_length=150, verbose_name='rooms_flat')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Wales_rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(verbose_name='link')),
                ('link', models.URLField(verbose_name='link')),
                ('price', models.CharField(max_length=30, verbose_name='price')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('rooms_flat', models.CharField(max_length=150, verbose_name='rooms_flat')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
            ],
        ),
    ]
