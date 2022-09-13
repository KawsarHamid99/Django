# Generated by Django 3.2 on 2022-09-07 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clr', models.CharField(max_length=30)),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parents_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.parents')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
            ],
            bases=('myapp.parents',),
        ),
    ]
