# Generated by Django 3.2 on 2022-12-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ModelsRelationship_2', '0004_auto_20221210_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='St',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('fees', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]