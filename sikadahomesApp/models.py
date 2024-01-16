from django.db import models
from django.utils import timezone

# from sikadahomesApp.views import locations

class AllProperties(models.Model):
    property_id = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    price = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.property_id



BUILDING_TYPE_CHOICES = (
    ('Apartment', 'Apartment'),
    ('Single_Room', 'Single Room')
)
class HouseRent(models.Model):
    # id = models.CharField(primary_key = True, max_length=100)
    property_id = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=30)
    type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='house_rent', max_length=10)
    price = models.IntegerField()
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
    property_id = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=30)
    type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='house_sale', max_length=10)
    price = models.IntegerField() 
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
    property_id = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=30)
    # type = models.CharField(choices=TYPE_CHOICES, max_length=50) 
    status = models.CharField(default='land_sale', max_length=10)
    price = models.IntegerField() 
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
    

class Feedback(models.Model):
    message = models.CharField(max_length=500, blank=True, null= True)
    status = models.CharField(max_length=200, blank=True, null= True)
    name  = models.CharField(max_length=200, blank=True, null= True)  



class Wishlist(models.Model):
    # id - models.CharField()
    property_id = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length = 100, null=True, blank=True)
    date_time = models.DateTimeField(default = timezone.now)