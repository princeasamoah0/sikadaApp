from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
import re
from .models import HouseRent,HouseSale,LandSale

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
    # import uuid
    # print (uuid.uuid4())
    # {'Rent_House':lastHouseRent, 'House_Sale':lastHouseSale}
    return render(request, 'index.html',{'lastHouseRent':lastHouseRent, 
                                         'previousLastHouseRent':previousLastHouseRent,
                                         'lastHouseSale':lastHouseSale,
                                         'previousLastHouseSale':previousLastHouseSale,
                                         'lastLandSale':lastLandSale,
                                         'previousLastLandSale':previousLastLandSale                                         
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
    return render(request, 'shop-right-sidebar.html')

def shop(request):
    return render(request, 'shop.html')

def team_details(request):
    return render(request, 'team-details.html')

def team(request):
    return render(request, 'team.html')

def wishlist(request):
    return render(request, 'wishlist.html')






















