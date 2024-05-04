from django.contrib import admin
from .models import (HouseRent,HouseSale,HouseLease,LandSale, AllProperties, Feedback, Wishlist,
                        MailingList, Message, Cart, Orders, UserDetails)

# Register your models here.

class RenderingAllProperties(admin.ModelAdmin):
    list_display = ('property_id','property_type', 'price', 'location')

class RenderingHouseRent(admin.ModelAdmin):
    list_display = ('property_id', 'property_title')

class RenderingHouseSale(admin.ModelAdmin):
    list_display = ('property_id', 'property_title') 

class RenderingLandSale(admin.ModelAdmin):
    list_display = ('property_id', 'property_title') 

class RenderingFeedback(admin.ModelAdmin):
    list_display = ("message", "status", "name")  


class RenderingCart(admin.ModelAdmin):
    list_display = ("user", "property_id", "status", "date_time")      

          
admin.site.site_header = 'Sikada Homes Admin Dashboard'


admin.site.register(AllProperties, RenderingAllProperties)
admin.site.register(HouseRent, RenderingHouseRent)
admin.site.register(HouseSale, RenderingHouseSale)
admin.site.register(HouseLease)
admin.site.register(LandSale, RenderingLandSale)
admin.site.register(Feedback, RenderingFeedback)
admin.site.register(Wishlist)
admin.site.register(MailingList)
admin.site.register(Message)
admin.site.register(Orders)
admin.site.register(Cart, RenderingCart)
admin.site.register(UserDetails)
