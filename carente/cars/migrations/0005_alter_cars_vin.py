# Generated by Django 3.2.7 on 2021-10-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_cars_gearbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='vin',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='شماره VIN خودرو'),
        ),
    ]
