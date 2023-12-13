from django.db import models

# from sikadahomesApp.views import locations
BUILDING_TYPE_CHOICES = (
    ('Apartment', 'Apartment'),
    ('Single_Room', 'Single Room')
)
class HouseRent(models.Model):
    # id = models.CharField(primary_key = True, max_length=100)
    title = models.CharField(null=True, blank=True, max_length=30)
    type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='rent', max_length=10)
    price = models.CharField(max_length=50) 
    location = models.CharField(max_length=100) 
    sub_location = models.CharField(max_length=100) 
    description = models.TextField()
    gps_address = models.CharField(max_length=20)
    image_1 = models.ImageField(upload_to='houseRent')
    image_2 = models.ImageField(upload_to='houseRent')
    image_3 = models.ImageField(upload_to='houseRent')
    image_4 = models.ImageField(upload_to='houseRent')
    image_5 = models.ImageField(upload_to='houseRent')
    video = models.ImageField(upload_to='houseRent')
    # Boolean
    pool = models.BooleanField()
    car_park = models.BooleanField()
    # Numerical 
    rooms = models.CharField(max_length=50)
    bed = models.CharField(max_length=10,null=True, blank=True)
    building_size = models.CharField(max_length=10,null=True, blank=True)
    land_size = models.CharField(max_length=10,null=True, blank=True)
    bath = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.title

#     other_amenities


class HouseSale(models.Model):
    title = models.CharField(null=True, blank=True, max_length=30)
    type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='sale', max_length=10)
    price = models.CharField(max_length=50) 
    location = models.CharField(max_length=100) 
    sub_location = models.CharField(max_length=100) 
    description = models.TextField()
    gps_address = models.CharField(max_length=20)
    image_1 = models.ImageField(upload_to='houseRent')
    image_2 = models.ImageField(upload_to='houseRent')
    image_3 = models.ImageField(upload_to='houseRent')
    image_4 = models.ImageField(upload_to='houseRent')
    image_5 = models.ImageField(upload_to='houseRent')
    video = models.ImageField(upload_to='houseRent')
    # Boolean
    pool = models.BooleanField()
    car_park = models.BooleanField()
    # Numerical 
    rooms = models.CharField(max_length=50)
    bed = models.CharField(max_length=10,null=True, blank=True)
    building_size = models.CharField(max_length=10,null=True, blank=True)
    land_size = models.CharField(max_length=10,null=True, blank=True)
    bath = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.title

    
class LandSale(models.Model):
    title = models.CharField(null=True, blank=True, max_length=30)
    # type = models.CharField(choices=TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='sale', max_length=10)
    price = models.CharField(max_length=50) 
    location = models.CharField(max_length=100) 
    sub_location = models.CharField(max_length=100) 
    description = models.TextField()
    gps_address = models.CharField(max_length=20)
    image_1 = models.ImageField(upload_to='houseRent')
    image_2 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    image_3 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    image_4 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    image_5 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    video = models.ImageField(upload_to='houseRent', null=True, blank=True)
    # Boolean
    serviced = models.BooleanField()
    fenced = models.BooleanField()
    # Numerical 
 
    land_size = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.title

# LandRent

