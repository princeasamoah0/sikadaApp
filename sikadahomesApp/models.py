from django.db import models
from django.utils import timezone

# from sikadahomesApp.views import locations

class AllProperties(models.Model):
    property_id = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    property_title = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.property_id



# BUILDING_TYPE_CHOICES = (
#     ('Apartment', 'Apartment'),
#     ('Single_Room', 'Single Room')
# )

# class HouseRent(models.Model):
#     # id = models.CharField(primary_key = True, max_length=100)
#     property_id = models.CharField(max_length=20, null=True, blank=True)
#     title = models.CharField(null=True, blank=True, max_length=30)
#     type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
#     status = models.CharField(default='house_rent', max_length=10)
#     price = models.IntegerField()
#     location = models.CharField(max_length=100) 
#     sub_location = models.CharField(max_length=100) 
#     description = models.TextField()
#     gps_address = models.CharField(max_length=20)
#     image_1 = models.ImageField(upload_to='houseRent')
#     image_2 = models.ImageField(upload_to='houseRent')
#     image_3 = models.ImageField(upload_to='houseRent')
#     image_4 = models.ImageField(upload_to='houseRent')
#     image_5 = models.ImageField(upload_to='houseRent')
#     video = models.ImageField(upload_to='houseRent')
#     # Boolean
#     pool = models.BooleanField()
#     car_park = models.BooleanField()
#     # Numerical 
#     rooms = models.CharField(max_length=50)
#     bed = models.CharField(max_length=10,null=True, blank=True)
#     building_size = models.CharField(max_length=10,null=True, blank=True)
#     land_size = models.CharField(max_length=10,null=True, blank=True)
#     bath = models.CharField(max_length=10,null=True, blank=True)

#     def __str__(self):
#         return self.title
    

class HouseRent(models.Model): 
    def image_upload_path(instance, filename):
        return "HouseRent"+"/"+str(instance.property_id)+"/"+filename   
    property_id = models.CharField(max_length=100,null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    budget = models.CharField(max_length=30, null=True, blank=True)
    img_listing = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_front = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    price = models.CharField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=100,null=True, blank=True)
    property_title = models.CharField(max_length=200, null=True, blank=True)
    property_address = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    home_area = models.CharField(max_length=100, null=True, blank=True)
    rooms = models.CharField(max_length=100,null=True, blank=True)
    baths = models.CharField(max_length=100,null=True, blank=True)
    year_built = models.CharField(max_length=100,null=True, blank=True)
    neigbourhood = models.CharField(max_length=100, null=True, blank=True)
    lot_dimensions = models.CharField(max_length=100, null=True, blank=True)
    beds = models.CharField(max_length=100,null=True, blank=True)
    balcony = models.CharField(max_length=100, null=True, blank=True)
    furnished = models.CharField(max_length=100, null=True, blank=True)
    completed = models.CharField(max_length=100, null=True, blank=True)
    living_room = models.CharField(max_length=100, null=True, blank=True)
    dining_area = models.CharField(max_length=100, null=True, blank=True)
    garden = models.CharField(max_length=100, null=True, blank=True)
    gym = models.CharField(max_length=100, null=True, blank=True)
    img_gallery_1 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_2 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_3 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    air_conditioner = models.CharField(max_length=100, null=True, blank=True)
    pool = models.CharField(max_length=100, null=True, blank=True)
    wifi = models.CharField(max_length=100, null=True, blank=True)
    near_church = models.CharField(max_length=100, null=True, blank=True)
    near_estate = models.CharField(max_length=100, null=True, blank=True)
    dish_washer = models.CharField(max_length=100, null=True, blank=True)
    security = models.CharField(max_length=100, null=True, blank=True)
    indoor_game = models.CharField(max_length=100, null=True, blank=True)
    cable_tv = models.CharField(max_length=100, null=True, blank=True)
    microwave = models.CharField(max_length=100, null=True, blank=True)
    date_time = models.DateTimeField(default = timezone.now)
    admin = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return self.property_title

class HouseSale(models.Model):
    def image_upload_path(instance, filename):
        return "HouseSale"+"/"+str(instance.property_id)+"/"+filename
    property_id = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    budget = models.CharField(max_length=30, null=True, blank=True)
    img_listing = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_front = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    price = models.CharField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=100,null=True, blank=True)
    property_title = models.CharField(max_length=200, null=True, blank=True)
    property_address = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    home_area = models.CharField(max_length=100, null=True, blank=True)
    rooms = models.CharField(max_length=100,null=True, blank=True)
    baths = models.CharField(max_length=100,null=True, blank=True)
    year_built = models.CharField(max_length=100,null=True, blank=True)
    neigbourhood = models.CharField(max_length=100, null=True, blank=True)
    lot_dimensions = models.CharField(max_length=100, null=True, blank=True)
    beds = models.CharField(max_length=100,null=True, blank=True)
    balcony = models.CharField(max_length=100, null=True, blank=True)
    furnished = models.CharField(max_length=100, null=True, blank=True)
    completed = models.CharField(max_length=100, null=True, blank=True)
    living_room = models.CharField(max_length=100, null=True, blank=True)
    dining_area = models.CharField(max_length=100, null=True, blank=True)
    garden = models.CharField(max_length=100, null=True, blank=True)
    gym = models.CharField(max_length=100, null=True, blank=True)
    img_gallery_1 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_2 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_3 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    air_conditioner = models.CharField(max_length=100, null=True, blank=True)
    pool = models.CharField(max_length=100, null=True, blank=True)
    wifi = models.CharField(max_length=100, null=True, blank=True)
    near_church = models.CharField(max_length=100, null=True, blank=True)
    near_estate = models.CharField(max_length=100, null=True, blank=True)
    dish_washer = models.CharField(max_length=100, null=True, blank=True)
    security = models.CharField(max_length=100, null=True, blank=True)
    indoor_game = models.CharField(max_length=100, null=True, blank=True)
    cable_tv = models.CharField(max_length=100, null=True, blank=True)
    microwave = models.CharField(max_length=100, null=True, blank=True)
    date_time = models.DateTimeField(default = timezone.now)
    admin = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return self.property_title

class HouseLease(models.Model):
    def image_upload_path(instance, filename):
        return "HouseLease"+"/"+str(instance.property_id)+"/"+filename
    property_id = models.CharField(max_length=100,null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    budget = models.CharField(max_length=30, null=True, blank=True)
    img_listing = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_front = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    price = models.CharField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=100,null=True, blank=True)
    property_title = models.CharField(max_length=200, null=True, blank=True)
    property_address = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    home_area = models.CharField(max_length=100, null=True, blank=True)
    rooms = models.CharField(max_length=100,null=True, blank=True)
    baths = models.CharField(max_length=100,null=True, blank=True)
    year_built = models.CharField(max_length=100,null=True, blank=True)
    neigbourhood = models.CharField(max_length=100, null=True, blank=True)
    lot_dimensions = models.CharField(max_length=100, null=True, blank=True)
    beds = models.CharField(max_length=100,null=True, blank=True)
    balcony = models.CharField(max_length=100, null=True, blank=True)
    furnished = models.CharField(max_length=100, null=True, blank=True)
    completed = models.CharField(max_length=100, null=True, blank=True)
    living_room = models.CharField(max_length=100, null=True, blank=True)
    dining_area = models.CharField(max_length=100, null=True, blank=True)
    garden = models.CharField(max_length=100, null=True, blank=True)
    gym = models.CharField(max_length=100, null=True, blank=True)
    img_gallery_1 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_2 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_gallery_3 = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    air_conditioner = models.CharField(max_length=100, null=True, blank=True)
    pool = models.CharField(max_length=100, null=True, blank=True)
    wifi = models.CharField(max_length=100, null=True, blank=True)
    near_church = models.CharField(max_length=100, null=True, blank=True)
    near_estate = models.CharField(max_length=100, null=True, blank=True)
    dish_washer = models.CharField(max_length=100, null=True, blank=True)
    security = models.CharField(max_length=100, null=True, blank=True)
    indoor_game = models.CharField(max_length=100, null=True, blank=True)
    cable_tv = models.CharField(max_length=100, null=True, blank=True)
    microwave = models.CharField(max_length=100, null=True, blank=True)
    date_time = models.DateTimeField(default = timezone.now)
    admin = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return self.property_title

# class HouseSale(models.Model):
#     property_id = models.CharField(max_length=20, null=True, blank=True)
#     title = models.CharField(null=True, blank=True, max_length=30)
#     type = models.CharField(choices=BUILDING_TYPE_CHOICES, max_length=50) 
#     status = models.CharField(default='house_sale', max_length=10)
#     price = models.IntegerField() 
#     location = models.CharField(max_length=100) 
#     sub_location = models.CharField(max_length=100) 
#     description = models.TextField()
#     gps_address = models.CharField(max_length=20)
#     image_1 = models.ImageField(upload_to='houseRent')
#     image_2 = models.ImageField(upload_to='houseRent')
#     image_3 = models.ImageField(upload_to='houseRent')
#     image_4 = models.ImageField(upload_to='houseRent')
#     image_5 = models.ImageField(upload_to='houseRent')
#     video = models.ImageField(upload_to='houseRent')
#     # Boolean
#     pool = models.BooleanField()
#     car_park = models.BooleanField()
#     # Numerical 
#     rooms = models.CharField(max_length=50)
#     bed = models.CharField(max_length=10,null=True, blank=True)
#     building_size = models.CharField(max_length=10,null=True, blank=True)
#     land_size = models.CharField(max_length=10,null=True, blank=True)
#     bath = models.CharField(max_length=10,null=True, blank=True)

#     def __str__(self):
#         return self.title

    
class LandSale(models.Model):
    def image_upload_path(instance, filename):
        return "LandSale"+"/"+str(instance.property_id)+"/"+filename
    property_id = models.CharField(max_length=20, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True) 
    location = models.CharField(max_length=100, blank = True, null = True) 
    property_title = models.CharField(null=True, blank=True, max_length=100)
    budget = models.CharField(max_length=30, null=True, blank=True)
    img_listing = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    img_front = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    date = models.CharField(max_length=100,null=True, blank=True)
    property_address = models.CharField(max_length=60, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True) 
    property_name = models.CharField(max_length=100, null=True, blank=True)
    commercial = models.CharField(max_length=100, null=True, blank=True)
    serviced = models.CharField(max_length=100, null=True, blank=True)
    fenced = models.CharField(max_length=100, null=True, blank=True)
    water = models.CharField(max_length=100, null=True, blank=True)
    electricity = models.CharField(max_length=100, null=True, blank=True)
    plot_dimensions = models.CharField(max_length=100, null=True, blank=True)
    no_of_plots = models.CharField(max_length=100, null=True, blank=True) 
    status = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank = True, null = True)
    date_time = models.DateTimeField(default = timezone.now)
    video_land = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    video_thumbnail = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    admin = models.CharField(max_length=100, blank = True, null = True)
    gps_address = models.CharField(max_length=20, blank = True, null = True)
    
    
    # image_3 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    # image_4 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    # image_5 = models.ImageField(upload_to='houseRent', null=True, blank=True)
    # video = models.ImageField(upload_to='houseRent', null=True, blank=True)
    # Boolean
    serviced = models.BooleanField()
    fenced = models.BooleanField()
    # Numerical 
 
    land_size = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.property_title

# LandRent
    

class Feedback(models.Model):
    message = models.CharField(max_length=500, blank=True, null= True)
    status = models.CharField(max_length=200, blank=True, null= True)
    name  = models.CharField(max_length=200, blank=True, null= True)  
    profile = models.ImageField(upload_to= 'Feedback/Profile', null=True, blank = True)



class Wishlist(models.Model):
    # id - models.CharField()
    property_id = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length = 100, null=True, blank=True)
    date_time = models.DateTimeField(default = timezone.now)
    def __str__ (self):
        return (self.username + " - " + self.property_id)

class Message(models.Model):
    name = models.CharField(max_length = 100, null=True, blank=True)
    email = models.CharField(max_length = 100, null=True, blank=True)
    message = models.TextField(null=True, blank = True)
    phone = models.CharField(max_length = 50, null=True, blank=True)
    service_type = models.CharField(max_length = 200, null=True, blank=True)
    save_my_mail = models.CharField(max_length = 50, null=True, blank=True)
    datetime = models.DateTimeField(default = timezone.now)  
    def __str__ (self):
        return self.email 


class MailingList(models.Model):
    email = models.CharField(max_length = 100, null=True, blank=True)
    name = models.CharField(max_length = 100, null=True, blank=True)
    isActive = models.CharField(max_length = 50, null=True, blank=True)
    datetime = models.DateTimeField(default = timezone.now)  
    def __str__ (self):
        return self.email 
    
    

class Cart(models.Model):
    user = models.CharField(max_length= 200, null=True, blank=True)
    property_id = models.TextField(null=True, blank=True)
    status = models.CharField(default='active', max_length=100)
    date_time = models.DateTimeField(default= timezone.now)


class Orders(models.Model):
    user = models.CharField(max_length= 200, null=True, blank=True)
    order_id = models.CharField(max_length=200, null=True, blank=True)
    property_id = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    company_address = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=200, null=True, blank=True)
    order_notes = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, default='pending', null=True, blank=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    date_time = models.DateTimeField(default= timezone.now)
    # def __str__ (self):
    #     return self.property_id