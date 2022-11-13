# Generated by Django 4.1.1 on 2022-10-03 23:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dados', models.FloatField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.tiposensor')),
            ],
        ),
    ]
