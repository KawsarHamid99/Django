# Generated by Django 3.2 on 2022-09-20 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelRelationship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='modelRelationship.user')),
                ('page_name', models.CharField(max_length=70)),
                ('page_cat', models.CharField(max_length=70)),
                ('page_publish_date', models.DateField()),
            ],
        ),
    ]
