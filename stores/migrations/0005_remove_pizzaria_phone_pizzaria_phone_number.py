# Generated by Django 5.0.1 on 2024-02-05 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_pizzaria_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaria',
            name='phone',
        ),
        migrations.AddField(
            model_name='pizzaria',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\1?\\d{9,10}$')]),
        ),
    ]