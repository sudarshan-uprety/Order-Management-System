# Generated by Django 4.2.2 on 2023-08-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beakerycategory',
            name='name',
            field=models.CharField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='drinkcategory',
            name='name',
            field=models.CharField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='name',
            field=models.CharField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='hukkacategory',
            name='name',
            field=models.CharField(max_length=55, unique=True),
        ),
    ]
