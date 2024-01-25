# Generated by Django 5.0.1 on 2024-01-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_bank_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='address1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
