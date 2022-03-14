# Generated by Django 3.2.7 on 2021-10-05 17:56

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelcar', models.CharField(max_length=20, verbose_name='مدل ماشین')),
                ('tozihat', models.TextField(verbose_name='توضیحات')),
                ('vin', models.IntegerField(verbose_name='شماره VIN خودرو')),
                ('available', models.BooleanField(default=1, verbose_name='آمادگی برای اجاره')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ اضافه شدن به سایت')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('shasinumber', models.IntegerField(verbose_name='شماره شاسی')),
                ('priceperday', models.IntegerField(verbose_name='قیمت اجاره روزانه به تومان')),
                ('gearbox', models.BooleanField(default=0, verbose_name='جعبه دنده ')),
                ('gearbox2', multiselectfield.db.fields.MultiSelectField(choices=[('dandei', 'دنده ای'), ('automatic', 'اتوماتیک')], max_length=16)),
                ('saltolid', models.DateField(default=1, verbose_name='سال تولید')),
                ('karkard', models.IntegerField(default=50, verbose_name='کارکرد')),
                ('pelak', models.CharField(max_length=20, verbose_name='پلاک')),
                ('city', models.CharField(max_length=20, verbose_name='شهر')),
                ('pricecar', models.IntegerField(verbose_name='قیمت تقریبی ماشین')),
                ('zabt', models.BooleanField(default=0, verbose_name='ضبط صوتی')),
                ('sahebcar', models.CharField(max_length=20, verbose_name='نام صاحب ماشین')),
            ],
            options={
                'verbose_name': 'ماشین',
                'verbose_name_plural': 'ماشین ها',
            },
        ),
    ]