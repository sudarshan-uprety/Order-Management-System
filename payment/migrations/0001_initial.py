# Generated by Django 4.2.2 on 2023-09-05 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0015_rename_bakeryquantity_bakeryorder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafePayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
            ],
        ),
    ]
