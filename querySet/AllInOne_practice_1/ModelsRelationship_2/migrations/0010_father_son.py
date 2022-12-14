# Generated by Django 3.2 on 2022-12-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsRelationship_2', '0009_child_parents'),
    ]

    operations = [
        migrations.CreateModel(
            name='father',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
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
            bases=('ModelsRelationship_2.father',),
        ),
    ]
