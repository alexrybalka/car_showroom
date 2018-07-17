# Generated by Django 2.0.7 on 2018-07-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_showroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclepart',
            name='description',
            field=models.TextField(default='Add some description', max_length=1000),
        ),
        migrations.AlterField(
            model_name='vehiclepart',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]