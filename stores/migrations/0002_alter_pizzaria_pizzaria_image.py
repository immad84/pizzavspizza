# Generated by Django 5.0.1 on 2024-02-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaria',
            name='pizzaria_image',
            field=models.ImageField(blank=True, upload_to='pizzariaImages'),
        ),
    ]