# Generated by Django 4.2.2 on 2023-08-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_bakerycategory_options_alter_beakery_options_and_more'),
        ('order', '0005_alter_order_order_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='HukkaQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.hukka')),
            ],
        ),
        migrations.CreateModel(
            name='FoodQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.food')),
            ],
        ),
        migrations.CreateModel(
            name='DrinksQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.drink')),
            ],
        ),
        migrations.CreateModel(
            name='BakeryQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.beakery')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='bakery',
            field=models.ManyToManyField(to='order.bakeryquantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='drink',
            field=models.ManyToManyField(to='order.drinksquantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.ManyToManyField(to='order.foodquantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='hukka',
            field=models.ManyToManyField(to='order.hukkaquantity'),
        ),
    ]
