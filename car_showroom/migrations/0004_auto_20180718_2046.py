# Generated by Django 2.0.7 on 2018-07-18 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_showroom', '0003_auto_20180718_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogue',
            name='price',
        ),
        migrations.RemoveField(
            model_name='catalogue',
            name='pub_date',
        ),
    ]
