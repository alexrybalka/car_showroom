# Generated by Django 2.0.7 on 2018-07-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_showroom', '0006_section_vehiclepart'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiclePartList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiclepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_showroom.VehiclePart')),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='vehiclepart',
        ),
        migrations.AddField(
            model_name='section',
            name='vehiclepartlist',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='car_showroom.VehiclePartList'),
            preserve_default=False,
        ),
    ]