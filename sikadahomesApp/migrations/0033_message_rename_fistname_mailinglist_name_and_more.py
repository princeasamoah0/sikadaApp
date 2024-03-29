# Generated by Django 5.0.1 on 2024-03-06 22:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0032_mailinglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='mailinglist',
            old_name='fistName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='lastName',
        ),
    ]
