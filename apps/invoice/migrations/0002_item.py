# Generated by Django 5.0.1 on 2024-01-19 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('full_weight', models.IntegerField(default=1)),
                ('net_weight', models.IntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('making_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(default=0)),
                ('stone_price', models.IntegerField(default=0)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.invoice')),
            ],
        ),
    ]
