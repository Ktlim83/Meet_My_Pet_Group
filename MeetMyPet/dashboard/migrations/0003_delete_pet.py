# Generated by Django 2.2 on 2020-08-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_pet_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pet',
        ),
    ]