# Generated by Django 4.2.7 on 2024-01-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0023_alter_allproperties_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='houselease',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
