# Generated by Django 4.2.2 on 2023-08-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_beakerycategory_name_alter_drinkcategory_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BeakeryCategory',
            new_name='BakeryCategory',
        ),
    ]
