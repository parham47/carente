# Generated by Django 3.2.7 on 2021-10-08 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20211008_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='gearbox',
        ),
    ]
