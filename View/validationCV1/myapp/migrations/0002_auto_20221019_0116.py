# Generated by Django 3.2 on 2022-10-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Names'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=100, verbose_name='Rolls'),
        ),
    ]