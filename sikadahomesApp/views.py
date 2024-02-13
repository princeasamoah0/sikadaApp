from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re
from django.http import JsonResponse

from itertools import chain
import random
from .models import HouseRent,HouseSale,HouseLease,LandSale,AllProperties,Feedback, Wishlist

# Create your views here.

def index (request):
    houseRent = HouseRent.objects.all().order_by('-id')[:2]
    houseSale = HouseSale.objects.all().order_by('-id')[:2]
    landSale = LandSale.objects.all().order_by('-id')[:2]
    feedback = Feedback.objects.all().order_by('-id')[:4]

    latest_listings = list(chain(houseRent, houseSale,landSale))
    random.shuffle(latest_listings)
    return render(request, 'general/index.html', {'context':latest_listings, 'feedback':feedback })

def wishlist_Ajax(request):
    if request.method == 'POST':
        propety_id = request.POST.get('property_id')
        a = Wishlist(property_id = propety_id, username = request.user.username)
        a.save()
        # print(request)
        # print(number)
        # print(request)
    else:
        print('GET')    
    data = {'message': 'Hello, world!', 'data': [1, 2, 3]}  # Example data
    return JsonResponse(data)
    # return JsonResponse
def page_404 (request):
    
    return render(request, 'general/404.html')

def about(request):  
    feedback = Feedback.objects.all().order_by('-id')[:4]
    return render(request, 'general/about.html', {'feedback':feedback})

def account(request):
    return render(request, 'general/account.html')

def add_listing(request):
    return render(request, 'general/add-listing.html')

def blog_details(request):
    return render(request, 'general/blog-details.html')

def blog_grid(request):
    return render(request, 'general/blog-grid.html')

def blog_left_sidebar(request):
    return render(request, 'general/blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'general/blog-right-sidebar.html')

def blog(request):
    return render(request, 'general/blog.html')


def cart(request):
    return render(request, 'general/cart.html')

def checkout(request):
    return render(request, 'general/checkout.html')

def coming_soon(request):
    return render(request, 'general/coming-soon.html')

def contact(request):
    return render(request, 'general/contact.html')

def faq(request):
    return render(request, 'general/faq.html')

def history(request):
    return render(request, 'general/history.html')

def locations(request):
    return render(request, 'general/locations.html')

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

    return render(request, 'general/login.html')

def logoutEvent(request):
    logout(request)
    return redirect(index)


def order_tracking(request):
    return render(request, 'general/order-tracking.html')

def portfolio_2(request):
    return render(request, 'general/portfolio-2.html')

def portfolio_details(request):
    return render(request, 'general/portfolio-details.html')

def portfolio(request):
    return render(request, 'general/portfolio.html')

def product_details(request,property_id):
    query = ''
    if HouseRent.objects.filter(property_id = property_id):
        query = HouseRent.objects.get(property_id = property_id)
    else:
        # HouseSale.objects.filter(property_id= property_id)
        query = HouseSale.objects.get(property_id= property_id)
    
    if query.status == 'house_for_rent':
        related_properties = HouseRent.objects.all().order_by('-id')[:2]
    else:
        related_properties = HouseSale.objects.all().order_by('-id')[:2]

    # else:
    #     query = LandSale.objects.get(property_id= property_id)

         
    print(query.status)
    return render(request, 'general/product-details.html', {'context':query, 'related_properties':related_properties} )

def land_details(request,pk):
    land_details = LandSale.objects.get(property_id = pk)
    related_properties = LandSale.objects.all().order_by('-id')[:2]
    # print(land_details.location)

    return render(request, 'general/land-details.html', {'context':land_details, 'related_properties':related_properties}, )
    
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
            return render(request, 'general/register.html')
        else:
            print('Here working')

        # except User.DoesNotExist:
            user= User.objects.create_user(phone, email, password, backend='django.contrib.auth.backends.ModelBackend')
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(index) 
            # return render(request, 'general/index.html')

            # print('User created successfully')



        # user = User.objects.create_user(phone, email, password)

    return render(request, 'general/register.html')

def service_details(request):
    return render(request, 'general/service-details.html')

def service(request):
    return render(request, 'general/service.html')

def shop_grid(request):
    return render(request, 'general/shop-grid.html')

def shop_left_sidebar(request):
    return render(request, 'general/shop-left-sidebar.html')

def shop_list(request):
    return render(request, 'general/shop-list.html')

def shop_right_sidebar(request):
    property_type = request.GET.get('property_type')
    location = request.GET.get('location') 
    # location = location.replace("_", " ") 
    # print(f"Location is {location}")
    price_range = request.GET.get('price_range')
    # print(property_type, location, price_range)
    call_all = ''

    # COUNTS
    count_house_for_sale = AllProperties.objects.filter(property_type = 'house_for_sale').count()
    count_house_for_rent= AllProperties.objects.filter(property_type = 'house_for_rent').count()
    count_house_for_lease= AllProperties.objects.filter(property_type = 'house_for_lease').count()
    count_land_for_sale= AllProperties.objects.filter(property_type = 'land_for_sale').count()

    count_greater_accra= AllProperties.objects.filter(location='Greater_Accra').count()
    count_ashanti= AllProperties.objects.filter(location='Ashanti_Region').count()
    count_northern= AllProperties.objects.filter(location='Northern_Region').count()
    count_eastern= AllProperties.objects.filter(location='Eastern_Region').count()
    count_central= AllProperties.objects.filter(location='Central_Region').count()
    count_western= AllProperties.objects.filter(location='Western_Region').count()
    count_upper_east= AllProperties.objects.filter(location='Upper_East').count()
    count_bono= AllProperties.objects.filter(location='Bono_Region').count()
    count_ahafo= AllProperties.objects.filter(location='Ahafo_Region').count()
    count_upper_west= AllProperties.objects.filter(location='Upper_West').count()
    count_volta= AllProperties.objects.filter(location='Volta_Region').count()
    count_bono_east= AllProperties.objects.filter(location='Bono_East').count()
    count_oti= AllProperties.objects.filter(location='Oti_Region').count()
    count_north_east= AllProperties.objects.filter(location='North_East').count()
    count_western_north= AllProperties.objects.filter(location='Western_North').count()
    count_savannah= AllProperties.objects.filter(location='Savannah_Region').count()


    counts = {'count_house_for_sale':count_house_for_sale, 'count_house_for_rent':count_house_for_rent,'count_house_for_lease':count_house_for_lease,
            'count_land_for_sale':count_land_for_sale,
            'count_greater_accra':count_greater_accra, 'count_ashanti':count_ashanti,
            'count_northern':count_northern,'count_eastern':count_eastern,'count_central':count_central,
            'count_western':count_western,'count_upper_east':count_upper_east,'count_bono':count_bono,
            'count_ahafo':count_ahafo,'count_upper_west':count_upper_west,'count_volta':count_volta,'count_bono_east':count_bono_east,
            'count_oti':count_oti,'count_north_east':count_north_east,'count_savannah':count_savannah, 'count_western_north':count_western_north,

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
    house_lease = HouseLease.objects.filter(property_id__in=querylist)
    land_sale = LandSale.objects.filter(property_id__in=querylist)


    all = list(chain(house_sale,house_rent,land_sale, house_lease))
    random.shuffle(all)
    print(f"chained {all}")
    
    print(property_type, location, price_range)

    context = {'property_type':property_type, 'location':location, 'price_range':price_range}

    if call_all == True:
        return render(request, 'general/shop-right-sidebar.html', {'context':context, 'data':all, 'counts':counts})
    elif house_sale.exists():
        return render(request, 'general/shop-right-sidebar.html', {'context':context, 'data':house_sale, 'counts':counts})
    elif house_lease.exists():
        return render(request, 'general/shop-right-sidebar.html', {'context':context, 'data':house_lease, 'counts':counts})
    elif house_rent.exists():
        return render(request, 'general/shop-right-sidebar.html', {'context':context, 'data':house_rent, 'counts':counts})
    elif land_sale.exists():
        return render(request, 'general/shop-right-sidebar.html', {'context':context, 'data':land_sale, 'counts':counts})

    # print(f"House sale {house_sale}, Land sale {land_sale}, House rent {house_rent}")


    return render(request, 'general/shop-right-sidebar.html', {'context':context, 'counts':counts, 'house_sale':house_sale, 'house_rent':house_rent, 'house_sale':house_sale})

def shop(request):
    return render(request, 'general/shop.html')

def team_details(request):
    return render(request, 'general/team-details.html')

def team(request):
    return render(request, 'general/team.html')

@login_required
def wishlist(request):
    data = Wishlist.objects.filter(username = request.user.username)
    querylist = [i.property_id for i in data]
    house_sale = HouseSale.objects.filter(property_id__in=querylist)
    house_rent = HouseRent.objects.filter(property_id__in=querylist)
    land_sale = LandSale.objects.filter(property_id__in=querylist)
    

    all = list(chain(house_sale,house_rent,land_sale))
    # random.shuffle(all)
    print(f"chained {all}")
    # print(querylist)
    return render(request, 'general/wishlist.html',  {'data': all})






















