# Generated by Django 2.2 on 2020-08-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.CharField(max_length=255, null=True)),
                ('bio', models.CharField(max_length=255, null=True)),
                ('pet', models.CharField(max_length=255, null=True)),
                ('pet_age', models.CharField(max_length=255, null=True)),
                ('pet_temperament', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('confirm', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
