# Generated by Django 3.2 on 2022-09-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuerySetApi_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('empnum', models.IntegerField()),
                ('dept', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
