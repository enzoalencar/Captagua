# Generated by Django 4.1.1 on 2022-10-03 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='tipo',
            new_name='tipos',
        ),
    ]
