# Generated by Django 4.2.2 on 2023-08-26 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_remove_order_items_order_bakery_order_drink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
