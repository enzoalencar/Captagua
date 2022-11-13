# Generated by Django 4.1.1 on 2022-10-16 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_tipos_sensor_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorFluxo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dados', models.FloatField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SensorUmidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dados', models.FloatField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
        migrations.DeleteModel(
            name='TipoSensor',
        ),
    ]
