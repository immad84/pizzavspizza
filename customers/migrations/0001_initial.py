# Generated by Django 5.0.1 on 2024-02-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_firstName', models.CharField(blank=True, max_length=100)),
                ('customer_lastName', models.CharField(blank=True, max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=100)),
            ],
        ),
    ]
