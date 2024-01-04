from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re

from itertools import chain
import random
from .models import HouseRent,HouseSale,LandSale,AllProperties,Feedback

# Create your views here.

def index (request):
    houseRent = HouseRent.objects.all().order_by('-id')[:2]
    lastHouseRent = houseRent[0]
    previousLastHouseRent = houseRent[1]

    houseSale = HouseSale.objects.all().order_by('-id')[:2]
    lastHouseSale = houseSale[0]
    previousLastHouseSale = houseSale[1]

    landSale = LandSale.objects.all().order_by('-id')[:2]
    lastLandSale = landSale[0]
    previousLastLandSale = landSale[1]

    feedback = Feedback.objects.all().order_by('-id')[:4]

    # import uuid
    # print (uuid.uuid4())
    # {'Rent_House':lastHouseRent, 'House_Sale':lastHouseSale}
    return render(request, 'index.html',{'lastHouseRent':lastHouseRent, 
                                         'previousLastHouseRent':previousLastHouseRent,
                                         'lastHouseSale':lastHouseSale,
                                         'previousLastHouseSale':previousLastHouseSale,
                                         'lastLandSale':lastLandSale,
                                         'previousLastLandSale':previousLastLandSale,
                                         'feedback':feedback                                       
                                         } )

def page_404 (request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def account(request):
    return render(request, 'account.html')

def add_listing(request):
    return render(request, 'add-listing.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'blog-right-sidebar.html')

def blog(request):
    return render(request, 'blog.html')


def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def history(request):
    return render(request, 'history.html')

def locations(request):
    return render(request, 'locations.html')

def login_view(request):
    if request.method == "POST":
        signIn_Param = request.POST['signIn_Param']
        password = request.POST['password']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, signIn_Param):
            try:
                user = User.objects.get(email = signIn_Param)
                user = authenticate(request, username=user.username, password=password) 
                if user is not None:
                    login(request, user)
                    return redirect(index)
                else:
                    messages.error(request, "Invalid Password") 
            except:            
                messages.error(request, "No account associated with this email")                   
        else:
            user = authenticate(request, username=signIn_Param, password=password)        
            if user is not None:
                login(request, user) 
                if request.GET.get('next'):
                    return redirect(wishlist)
                else:
                    return redirect(index)    
            else:
                messages.error(request, "Invalid Login Credentials")
    
    return render(request, 'login.html')

def logoutEvent(request):
    logout(request)
    return redirect(index)


def order_tracking(request):
    return render(request, 'order-tracking.html')

def portfolio_2(request):
    return render(request, 'portfolio-2.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def product_details(request,search_type,pk):
    houseDetail = HouseSale.objects.get(pk = pk)
    # print(house_detail)
    return render(request, 'product-details.html', {'houseDetail':houseDetail} )

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        # try:
        checkUserName = User.objects.filter(Q(username=phone) | Q(email=email))
        if checkUserName.count() != 0:
            messages.error(request, "Phone number or email already exists") 
            return render(request, 'register.html')
        else:
            print('Here working')
            
        # except User.DoesNotExist:
            user= User.objects.create_user(phone, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            login(request, user)
            return redirect(index) 
            # return render(request, 'index.html')

            # print('User created successfully')

      
        
        # user = User.objects.create_user(phone, email, password)
       
    return render(request, 'register.html')

def service_details(request):
    return render(request, 'service-details.html')

def service(request):
    return render(request, 'service.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def shop_left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')

def shop_list(request):
    return render(request, 'shop-list.html')

def shop_right_sidebar(request):
    property_type = request.GET.get('property_type')
    location = request.GET.get('location')
    price_range = request.GET.get('price_range')
    call_all = ''



    # COUNTS
    count_house_for_sale = AllProperties.objects.filter(property_type = 'house_for_sale').count()
    count_house_for_rent= AllProperties.objects.filter(property_type = 'house_for_rent').count()
    count_land_for_sale= AllProperties.objects.filter(property_type = 'land_for_sale').count()
   
    count_greater_accra= AllProperties.objects.filter(location='greater_accra').count()
    count_ashanti= AllProperties.objects.filter(location='ashanti').count()
    count_northern= AllProperties.objects.filter(location='northern').count()
    count_eastern= AllProperties.objects.filter(location='eastern').count()
    count_central= AllProperties.objects.filter(location='central').count()
    count_western= AllProperties.objects.filter(location='western').count()
    count_upper_east= AllProperties.objects.filter(location='upper_east').count()
    count_bono= AllProperties.objects.filter(location='bono').count()
    count_ahafo= AllProperties.objects.filter(location='ahafo').count()
    count_bono_west= AllProperties.objects.filter(location='bono_west').count()
    count_volta= AllProperties.objects.filter(location='volta').count()
    count_bono_east= AllProperties.objects.filter(location='bono_east').count()
    count_oti= AllProperties.objects.filter(location='oti').count()
    count_north_east= AllProperties.objects.filter(location='north_east').count()
    count_savannah= AllProperties.objects.filter(location='savannah').count()
    

    counts = {'count_house_for_sale':count_house_for_sale, 'count_house_for_rent':count_house_for_rent,'count_land_for_sale':count_land_for_sale,
            'count_greater_accra':count_greater_accra, 'count_ashanti':count_ashanti,
            'count_northern':count_northern,'count_eastern':count_eastern,'count_central':count_central,
            'count_western':count_western,'count_upper_east':count_upper_east,'count_bono':count_bono,
            'count_ahafo':count_ahafo,'count_bono_west':count_bono_west,'count_volta':count_volta,'count_bono_east':count_bono_east,
            'count_oti':count_oti,'count_north_east':count_north_east,'count_savannah':count_savannah
           
            }

    # print(count_house_for_sale,count_house_for_rent, count_land_for_sale)
    # house_sale_count = HouseSale.objects.all().count()
    # house_rent_count = HouseRent.objects.all().count()
    # land_sale.count = LandSale.objects.all().count()
    
    if(property_type == 'none' and location == 'none' and price_range == 'none'):
        query = AllProperties.objects.all()  
        call_all = True     
    elif(property_type != 'none' and location == 'none' and price_range == 'none'):
        query = AllProperties.objects.filter(property_type=property_type) 
    elif(property_type == 'none' and location != 'none' and price_range == 'none'):  
        query = AllProperties.objects.filter(location=location)  
    elif(property_type == 'none' and location != 'none' and price_range != 'none'): 
        if price_range == 'low_budget':
            query = AllProperties.objects.filter(location=location, price__lt = 10000)
            print(price_range) 
        elif price_range == 'medium_budget':
            query = AllProperties.objects.filter(location=location, price__gt=10000, price__lt=30000)
            print(price_range) 
        elif price_range == 'high_budget':
            query = AllProperties.objects.filter(location=location, price__gt=30000) 
            print(price_range)   
    elif(property_type != 'none' and location != 'none' and price_range == 'none'): 
        print(1) 
        query = AllProperties.objects.filter(property_type=property_type, location=location) 
    elif(property_type == 'none' and location == 'none' and price_range != 'none'): 
        print(4, price_range)
        if price_range == 'low_budget':
            print('low')
            # query = AllProperties.objects.filter(price__lt=10000)
            query = AllProperties.objects.filter(price__lt = 10000)
        elif price_range == 'medium_budget':
            print('mid')
            query = AllProperties.objects.filter(price__gt=10000, price__lt=30000)
        elif price_range == 'high_budget':
            print('high')
            query = AllProperties.objects.filter(price__gt=30000)

    elif(property_type != 'none' and location != 'none' and price_range != 'none'): 
        print(2, location)  
        if price_range == 'low_budget':
            query = AllProperties.objects.filter(property_type=property_type, location=location, price__lt=10000)
        elif price_range == 'medium_budget':
            query = AllProperties.objects.filter(property_type=property_type, location=location, price__gt=10000, price__lt=30000)
        elif price_range == 'high_budget':
            query = AllProperties.objects.filter(property_type=property_type, location=location, price__gt=30000)
    querylist = [i.property_id for i in query]
    # print(query)

    house_sale = HouseSale.objects.filter(property_id__in=querylist)
    house_rent = HouseRent.objects.filter(property_id__in=querylist)
    land_sale = LandSale.objects.filter(property_id__in=querylist)
    

    all = list(chain(house_sale,house_rent,land_sale))
    random.shuffle(all)
    print(f"chanined {all}")
    
    context = {'property_type':property_type, 'location':location, 'price_range':price_range}

    if call_all == True:
        return render(request, 'shop-right-sidebar.html', {'context':context, 'data':all, 'counts':counts})
    elif house_sale.exists():
        return render(request, 'shop-right-sidebar.html', {'context':context, 'data':house_sale, 'counts':counts})
    elif house_rent.exists():
        return render(request, 'shop-right-sidebar.html', {'context':context, 'data':house_rent, 'counts':counts})
    elif land_sale.exists():
        return render(request, 'shop-right-sidebar.html', {'context':context, 'data':land_sale, 'counts':counts})
    
    # print(f"House sale {house_sale}, Land sale {land_sale}, House rent {house_rent}")
    
    
    return render(request, 'shop-right-sidebar.html', {'context':context, 'counts':counts, 'house_sale':house_sale, 'house_rent':house_rent, 'house_sale':house_sale})

def shop(request):
    return render(request, 'shop.html')

def team_details(request):
    return render(request, 'team-details.html')

def team(request):
    return render(request, 'team.html')

@login_required
def wishlist(request):
    return render(request, 'wishlist.html')






















