# Generated by Django 5.0.1 on 2024-01-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_item_net_amount_alter_item_unit_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='making_charges_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
