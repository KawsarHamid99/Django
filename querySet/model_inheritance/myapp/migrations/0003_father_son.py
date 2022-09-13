# Generated by Django 3.2 on 2022-09-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_child_parents'),
    ]

    operations = [
        migrations.CreateModel(
            name='father',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('clr', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='son',
            fields=[
            ],
            options={
                'ordering': ['age'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.father',),
        ),
    ]
