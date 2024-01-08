from django.contrib import admin
from .models import HouseRent,HouseSale,LandSale, AllProperties, Feedback

# Register your models here.

class RenderingAllProperties(admin.ModelAdmin):
    list_display = ('property_id','property_type', 'price', 'location')

class RenderingHouseRent(admin.ModelAdmin):
    list_display = ('title','property_id', 'price', 'location')

class RenderingHouseSale(admin.ModelAdmin):
    list_display = ('title','property_id', 'price', 'location') 

class RenderingLandSale(admin.ModelAdmin):
    list_display = ('title','property_id', 'price', 'location') 

class RenderingFeedback(admin.ModelAdmin):
    list_display = ("message", "status", "name")        


admin.site.register(AllProperties, RenderingAllProperties)
admin.site.register(HouseRent, RenderingHouseRent)
admin.site.register(HouseSale,RenderingHouseSale)
admin.site.register(LandSale, RenderingLandSale)
admin.site.register(Feedback, RenderingFeedback)