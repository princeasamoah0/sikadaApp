# Generated by Django 4.2.7 on 2024-01-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0016_wishlist_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseLease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('budget', models.CharField(blank=True, max_length=30, null=True)),
                ('img_listing', models.ImageField(blank=True, null=True, upload_to='houseLease')),
                ('img_front', models.ImageField(blank=True, null=True, upload_to='houseLease')),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('property_title', models.CharField(blank=True, max_length=200, null=True)),
                ('property_address', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('property_name', models.CharField(blank=True, max_length=100, null=True)),
                ('home_area', models.CharField(blank=True, max_length=100, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('baths', models.IntegerField(blank=True, null=True)),
                ('year_built', models.IntegerField(blank=True, null=True)),
                ('neigbourhood', models.CharField(blank=True, max_length=100, null=True)),
                ('lot_dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('beds', models.IntegerField(blank=True, null=True)),
                ('balcony', models.CharField(blank=True, max_length=100, null=True)),
                ('furnished', models.CharField(blank=True, max_length=100, null=True)),
                ('completed', models.CharField(blank=True, max_length=100, null=True)),
                ('living_room', models.CharField(blank=True, max_length=100, null=True)),
                ('dining_area', models.CharField(blank=True, max_length=100, null=True)),
                ('garden', models.CharField(blank=True, max_length=100, null=True)),
                ('gym', models.CharField(blank=True, max_length=100, null=True)),
                ('img_gallery_1', models.ImageField(blank=True, null=True, upload_to='houseLease')),
                ('img_gallery_2', models.ImageField(blank=True, null=True, upload_to='houseLease')),
                ('img_gallery_3', models.ImageField(blank=True, null=True, upload_to='houseLease')),
                ('air_conditioner', models.CharField(blank=True, max_length=100, null=True)),
                ('pool', models.CharField(blank=True, max_length=100, null=True)),
                ('wifi', models.CharField(blank=True, max_length=100, null=True)),
                ('near_church', models.CharField(blank=True, max_length=100, null=True)),
                ('near_estate', models.CharField(blank=True, max_length=100, null=True)),
                ('dish_washer', models.CharField(blank=True, max_length=100, null=True)),
                ('security', models.CharField(blank=True, max_length=100, null=True)),
                ('indoor_game', models.CharField(blank=True, max_length=100, null=True)),
                ('cable_tv', models.CharField(blank=True, max_length=100, null=True)),
                ('microwave', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='bed',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='building_size',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='car_park',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='gps_address',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='land_size',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='location',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='property_id',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='sub_location',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='type',
        ),
        migrations.RemoveField(
            model_name='houserent',
            name='video',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='bed',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='building_size',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='car_park',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='gps_address',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='land_size',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='location',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='property_id',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='sub_location',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='title',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='type',
        ),
        migrations.RemoveField(
            model_name='housesale',
            name='video',
        ),
        migrations.AddField(
            model_name='houserent',
            name='air_conditioner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='balcony',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='baths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='budget',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='cable_tv',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='completed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='dining_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='dish_washer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='furnished',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='garden',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='gym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='home_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='img_front',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='img_gallery_1',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='img_gallery_2',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='img_gallery_3',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='img_listing',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AddField(
            model_name='houserent',
            name='indoor_game',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='living_room',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='lot_dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='microwave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='near_church',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='near_estate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='neigbourhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='property_address',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='property_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='property_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='security',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='wifi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houserent',
            name='year_built',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='air_conditioner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='balcony',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='baths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='budget',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='cable_tv',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='completed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='dining_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='dish_washer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='furnished',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='garden',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='gym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='home_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='img_front',
            field=models.ImageField(blank=True, null=True, upload_to='houseSale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='img_gallery_1',
            field=models.ImageField(blank=True, null=True, upload_to='houseSale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='img_gallery_2',
            field=models.ImageField(blank=True, null=True, upload_to='houseSale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='img_gallery_3',
            field=models.ImageField(blank=True, null=True, upload_to='houseSale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='img_listing',
            field=models.ImageField(blank=True, null=True, upload_to='houseSale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='indoor_game',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='living_room',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='lot_dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='microwave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='near_church',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='near_estate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='neigbourhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='property_address',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='property_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='property_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='security',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='wifi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='housesale',
            name='year_built',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='pool',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='pool',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
