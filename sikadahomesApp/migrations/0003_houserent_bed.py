# Generated by Django 4.2.7 on 2023-12-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0002_houserent_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='houserent',
            name='bed',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
