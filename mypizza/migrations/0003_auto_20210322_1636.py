# Generated by Django 3.1.7 on 2021-03-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypizza', '0002_customermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='phoneno',
            field=models.CharField(max_length=10),
        ),
    ]
