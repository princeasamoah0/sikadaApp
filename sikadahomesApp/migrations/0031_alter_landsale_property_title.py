# Generated by Django 3.2.16 on 2024-01-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0030_auto_20240128_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landsale',
            name='property_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
