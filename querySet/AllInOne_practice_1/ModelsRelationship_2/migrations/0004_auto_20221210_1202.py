# Generated by Django 3.2 on 2022-12-10 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsRelationship_2', '0003_city_interest_person_personaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='personaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='personaddress',
            name='person',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Personaddress',
        ),
    ]
