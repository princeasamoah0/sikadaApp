# Generated by Django 4.2.7 on 2023-12-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseRent',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Apartment', 'Apartment'), ('Single_Room', 'Single Room')], max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('sub_location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('gps_address', models.CharField(max_length=20)),
                ('image_1', models.ImageField(upload_to='houseRent')),
                ('image_2', models.ImageField(upload_to='houseRent')),
                ('image_3', models.ImageField(upload_to='houseRent')),
                ('image_4', models.ImageField(upload_to='houseRent')),
                ('image_5', models.ImageField(upload_to='houseRent')),
                ('video', models.ImageField(upload_to='houseRent')),
                ('pool', models.BooleanField()),
                ('car_park', models.BooleanField()),
                ('rooms', models.CharField(max_length=50)),
            ],
        ),
    ]
