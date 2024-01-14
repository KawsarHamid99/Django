# Generated by Django 5.0.1 on 2024-01-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.CharField(max_length=100, unique=True)),
                ('recommendade_RAM', models.ManyToManyField(blank=True, to='myapp.ram')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.CharField(max_length=100, unique=True)),
                ('recommendade_RAM', models.ManyToManyField(blank=True, to='myapp.ram')),
                ('recommendade_SSD', models.ManyToManyField(blank=True, to='myapp.ssd')),
            ],
        ),
    ]
