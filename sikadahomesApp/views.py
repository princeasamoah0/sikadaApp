from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re
from django.http import JsonResponse, HttpResponse

from itertools import chain
import random
from .models import ( HouseRent,HouseSale,HouseLease,LandSale,
                     AllProperties,Feedback, Wishlist,
                      MailingList,Message, Cart,Orders,
                      UserDetails
                    )
import secrets
import string 



def index (request):
    if 'userId' in request.session :
        print('Already have a session set.')
    else:    
        userId = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
        request.session['userId'] = userId
        print('No UserId, so new one has been set')
    
    if request.method == 'POST':
        email = request.POST['email']
        a = MailingList(email = email)
        a.save()
        print(email)
        messages.info(request, "Email added to mailing list.")
        # messages.error(request, "Invalid Login Credentials")
        # messages.error(request, "Phone number or email already exists")
        
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
    else:
        print('GET')    
    data = {'message': 'Hello, world!', 'data': [1, 2, 3]}  # Example data
    return JsonResponse(data)

def deleteWishlist_Ajax(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        try:
            item = Wishlist.objects.get(property_id = property_id)
            item.delete()            
        except item.DoesNotExist:
            JsonResponse({'message':'Something went wrong'})
    return JsonResponse({'message':'Something went wrong'})    
def page_404 (request):
    
    return render(request, 'general/404.html')

def about(request):  
    feedback = Feedback.objects.all().order_by('-id')[:4]
    return render(request, 'general/about.html', {'feedback':feedback})

@login_required
def account(request):
    if request.method == 'POST':
        if request.POST.get('current_password'):
            current_password = request.POST.get('current_password')
            confirm_password = request.POST.get('confirm_password')
            try:
                user = User.objects.get(username=request.user.username)
                if user.check_password(current_password):
                    user.set_password(confirm_password)
                    user.save()
                    messages.success(request, 'Password changed successfully.')
                else:
                    messages.error(request, 'Incorrect old password.')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')

    userdetails = UserDetails.objects.get(username = request.user.username)           
    return render(request, 'general/account.html', {'userdetails':userdetails})

def add_listing(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        price_range = request.POST.get('price_range')
        condition = request.POST.get('condition')
        property_type = request.POST.get('property_type')
        img_listing = request.FILES.get('img_listing')
        img_front = request.FILES.get('img_front')
        img_gallery_1 = request.FILES.get('img_gallery_1')
        img_gallery_2 = request.FILES.get('img_gallery_2')
        img_gallery_3 = request.FILES.get('img_gallery_3')
        property_address = request.POST.get('property_address')
        region = request.POST.get('region')
        location = request.POST.get('location')
        neigbourhood = request.POST.get('neigbourhood')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        air_conditioning = request.POST.get('air_conditioning') == 'on'
        swimming_pool = request.POST.get('swimming_pool') == 'on'
        wifi = request.POST.get('wifi') == 'on'
        near_church = request.POST.get('near_church') == 'on'
        near_estate = request.POST.get('near_estate') == 'on'
        dish_washer = request.POST.get('dish_washer') == 'on'
        security = request.POST.get('security') == 'on'
        indoor_game = request.POST.get('indoor_game') == 'on'
        cable_tv = request.POST.get('cable_tv') == 'on'
        microwave = request.POST.get('microwave') == 'on'


        def generate_random_id(length=10):
            import random
            import string
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(length))
        property_id = generate_random_id()

        if property_type == 'house_for_sale':
            a = HouseSale(property_id=property_id,location=location,
                            region=region, budget=price_range,img_listing=img_listing,img_front=img_front,
                            status=condition,price=price, 
                            property_title=title,property_address=property_address,description=description,
                            neigbourhood=neigbourhood,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                            wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                            security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                        )
            a.save()
        elif property_type == 'house_for_rent':
            a = HouseRent(property_id=property_id,location=location,
                            region=region, budget=price_range,img_listing=img_listing,img_front=img_front,
                            status=condition,price=price, 
                            property_title=title,property_address=property_address,description=description,
                            neigbourhood=neigbourhood,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                            wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                            security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                            )
            a.save()
        elif property_type == 'land_for_sale':
            print('Work it out for land for sale in Admin View') 
        else:
            a = HouseRent(property_id=property_id,location=location,
                            region=region, budget=price_range,img_listing=img_listing,img_front=img_front,
                            status=condition,price=price, 
                            property_title=title,property_address=property_address,description=description,
                            neigbourhood=neigbourhood,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                            wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                            security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                            )
            a.save()

        b = AllProperties(property_id=property_id,property_type=property_type,price=price,location=region, property_title = title)
        b.save() 
        messages.success(request,"Listing successfully added.")
        return redirect(index)
        print('Message Added')    
        # status = request.POST.get('')

        # print(f'''Posting Has started {title, description, price, price_range,
        #                              condition, property_type, img_listing, img_front,img_gallery_1,
        #                              img_gallery_2, img_gallery_3, property_address, region, location,
        #                              neigbourhood, latitude, longitude, air_conditioning,
        #                              swimming_pool, wifi, near_church, near_estate, dish_washer,
        #                              security, indoor_game, cable_tv, microwave}''')
    return render(request, 'general/add-listing.html')

def blog_details(request):
    return render(request, 'general/phg-form.html')
    # return render(request, 'general/blog-details.html')

def blog_grid(request):
    return render(request, 'general/blog-grid.html')

def blog_left_sidebar(request):
    return render(request, 'general/blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'general/blog-right-sidebar.html')

def blog(request):
    return render(request, 'general/blog.html')


def cart(request):
    cart_items = Cart.objects.filter(user = request.user, status = 'active')
    cart = cart_items.count()

    querylist = [i.property_id for i in cart_items]
    house_sale = HouseSale.objects.filter(property_id__in=querylist)
    house_rent = HouseRent.objects.filter(property_id__in=querylist)
    land_sale = LandSale.objects.filter(property_id__in=querylist)
    
    all = list(chain(house_sale,house_rent,land_sale))
    
    property_id = ''
    if len(all) > 1:
        for i in all[:-1]:
            property_id += i.property_id + ','
        property_id += all[-1].property_id
    else:
        try:
            property_id = all[0].property_id  
        except:
            pass
    total_price = 0
    for i in all:
        total_price += int(i.price)
     
    return render(request, 'general/cart.html', {'cart':cart, 'cart_items':all, 'total_price':total_price, 'property_id':property_id})

def checkout(request, property_id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        country = request.POST.get('country')
        address = request.POST.get('address')
        address_2 = request.POST.get('address_2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        order_notes = request.POST.get('order_notes')
        payment_method = request.POST.get('payment_method')

        def generate_unique_code():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            while Orders.objects.filter(order_id=code).exists():
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            return code 
        order_id = generate_unique_code()  
        a = Orders(first_name = first_name, payment_method=payment_method, user = request.user.username, property_id = property_id,order_id=order_id, last_name = last_name, email = email, phone = phone, company_name = company_name, company_address = company_address, country = country, address = address, address_2 = address_2, city = city, state = state, zip = zip, order_notes = order_notes)
        a.save()
        messages.success(request, "You have successfully placed your order")
        
        if ',' in property_id:
            property_ids = property_id.split(',')
            for i in property_ids:
                Cart.objects.filter(user = request.user, property_id = i, status = 'active' ).update(status = 'inactive')
        else:
            Cart.objects.filter(user = request.user, property_id = property_id, status = 'active' ).update(status = 'inactive')


    property_ids = property_id.split(',')
    # print(property_ids)
    all_items = [obj for i in property_ids for obj in AllProperties.objects.filter(property_id=i)]
    cart_count = len(all_items)
    total_price = sum(int(i.price) for i in all_items)


    

    return render(request, 'general/checkout.html', {'all_items':all_items, 'total_price':total_price, 'cart_count':cart_count})

def coming_soon(request):
    return render(request, 'general/coming-soon.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        save_my_mail = request.POST.get('save_my_mail')
        a = Message(name = name, email=email, message=message, phone=phone,
                service_type=service_type, save_my_mail=save_my_mail )
        a.save()
        messages.success(request, "Message Sent")
        # messages.(request, "Invalid Password")
        # print(name,email,service_type,phone,message,save_my_mail)
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
                    query = (request.GET.get('next'))[1:]
                    # print(f"The print statement is, {(request.GET.get('next'))[1:]}")
                    return redirect(query)
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


# @login_required
def add_to_cart(request):  
    property_id = request.POST.get('property_id')
    if request.user.is_authenticated:
        try:
            Cart.objects.get(user=request.user.username, property_id=property_id, status='active')
            return JsonResponse('already_added', safe=False)
        except Cart.DoesNotExist:
            a = Cart(property_id=property_id,user=request.user.username)
            a.save()
            # messages.success(request, "Property Successfully added to Cart")
            return JsonResponse('successfully_added', safe=False)
    else:
        return JsonResponse('unauthenticated', safe=False)


def fetch_cart_items(request):

    data = Cart.objects.filter(user=request.user.username, status='active') 
    querylist = [i.property_id for i in data]

    all_results = [
        {
        'property_id': result.property_id,
        'pk': result.pk,
        'price': result.price,
        'property_title': result.property_title,
        'img_listing': result.img_listing.url,
        # Add other fields you want to include in the response
        }
    for result in chain(
        HouseSale.objects.filter(property_id__in=querylist),
        HouseRent.objects.filter(property_id__in=querylist),
        HouseLease.objects.filter(property_id__in=querylist),
        LandSale.objects.filter(property_id__in=querylist)
        )
    ]

    return JsonResponse(all_results, safe=False)

def delete_cart_item(request):
    property_id = request.POST.get('property_id')
    item = Cart.objects.get(property_id=property_id, user=request.user.username, status='active')
    item.delete()
    return JsonResponse('deleted', safe=False)

def get_cart_count(request):
    # data = Cart.objects.all().count()
    data = Cart.objects.filter(user=request.user.username, status='active').count()

    # return JsonResponse(list(data), safe=False)
    return JsonResponse(data, safe=False)

def product_details(request,property_id):
    if request.method == 'POST':
        if request.POST.get('messageForm'):
            name = request.POST['yourname']
            email = request.POST['youremail']
            message = request.POST['yourmessage']
            a = Message(email=email, name = name, message=message)
            a.save()
            messages.success(request, "Message has been sent successfully.")
        elif request.POST.get('mailingListForm'):  
            email = request.POST['email'] 
            a = MailingList(email = email)
            a.save()
            messages.success(request, "Your email was successfully been addded.")
            print(f'My email is {email}')  
        else:
            pass

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

    cart = Cart.objects.filter(user = request.user.username)   
    # print(cart) 
         
    cart = Cart.objects.filter(user = request.user, status = 'active').count()
    return render(request, 'general/product-details.html', {'context':query, 'related_properties':related_properties, 'cart':cart} )

def land_details(request,pk):   
    land_details = LandSale.objects.get(property_id = pk)
    related_properties = LandSale.objects.all().order_by('-id')[:2]
    cart = Cart.objects.filter(user = request.user, status = 'active').count()
    return render(request, 'general/land-details.html', {'context':land_details, 'related_properties':related_properties, 'cart':cart}, )
    
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
        # try:    
        #     user= User.objects.create_user(phone, email, password, backend='django.contrib.auth.backends.ModelBackend')
        #     user.first_name = firstname
        #     user.last_name = lastname
        #     user.save()
        #     login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        #     return redirect(index) 
                
        # except:
        user= User.objects.create_user(phone, email, password)
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
    # if request.method == 'POST':
    #     name = request.POST['yourname']
    #     email = request.POST['youremail']
    #     message = request.POST['yourmessage']
    #     print("Working now")
    #     print(name, email, message)

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
    # print(f"chained {all}")
    return render(request, 'general/wishlist.html',  {'data': all})






















