# Generated by Django 4.1.2 on 2022-10-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=3000, null=True)),
                ('name', models.CharField(max_length=3000, null=True)),
            ],
        ),
    ]