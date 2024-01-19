# Generated by Django 5.0.1 on 2024-01-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('invoice', 'Invoice'), ('credit_note', 'Credit note')], default='invoice', max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sender_reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
