# Generated by Django 4.2.7 on 2023-12-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0004_houserent_building_size_houserent_land_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='houserent',
            name='bath',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
