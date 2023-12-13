from django.contrib import admin
from .models import HouseRent,HouseSale,LandSale

# Register your models here.

admin.site.register(HouseRent)
admin.site.register(HouseSale)
admin.site.register(LandSale)