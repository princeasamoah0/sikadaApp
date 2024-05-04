from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages
from sikadahomesApp.models import *

# Create your views here.
@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def index(request):
    if not request.user.is_staff:
        print('You dont have permission')
        raise PermissionDenied("You don't have permission to view this page.")
    
    return render(request, 'admin-app/index.html')
    # else:
    #     return redirect('sign-in')
    
@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def page_404(request):
    return render(request, 'admin-app/404.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def page_500(request):
    return render(request, 'admin-app/500.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def add_agent(request):
    return render(request, 'admin-app/add-agent.html')


def generate_random_id(length=10):
        import random
        import string
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))



def SaveFunction(request, param):    
        region = request.POST.get('region')
        budget = request.POST.get('budget')
        img_listing = request.FILES.get('img_listing')
        img_front = request.FILES.get('img_front')
        status = request.POST.get('status')
        price = request.POST.get('price')
        date = request.POST.get('date')
        property_title = request.POST.get('property_title')
        location = request.POST.get('location')
        property_address = request.POST.get('property_address')
        description = request.POST.get('description')
        property_name = request.POST.get('property_name')
        home_area = request.POST.get('home_area')
        rooms = request.POST.get('rooms')
        baths = request.POST.get('baths')
        year_built = request.POST.get('year_built')
        neigbourhood = request.POST.get('neigbourhood')
        lot_dimensions = request.POST.get('lot_dimensions')
        beds = request.POST.get('beds')
        balcony = request.POST.get('balcony')
        furnished = request.POST.get('furnished')
        completed = request.POST.get('completed')
        living_room = request.POST.get('living_room')
        dining_area = request.POST.get('dining_area')
        garden = request.POST.get('garden')
        gym = request.POST.get('gym')
        img_gallery_1 = request.FILES.get('img_gallery_1')
        img_gallery_2 = request.FILES.get('img_gallery_2')
        img_gallery_3 = request.FILES.get('img_gallery_3')
        air_conditioner = request.POST.get('air_conditioner') == 'on'
        pool = request.POST.get('pool') == 'on'
        wifi = request.POST.get('wifi') == 'on'
        near_church = request.POST.get('near_church') == 'on'
        near_estate = request.POST.get('near_estate') == 'on'
        dish_washer = request.POST.get('dish_washer') == 'on'
        security = request.POST.get('security') == 'on'
        indoor_game = request.POST.get('indoor_game') == 'on'
        cable_tv = request.POST.get('cable_tv') == 'on'
        microwave = request.POST.get('microwave') == 'on'
        # print(f''' Region = {region}, budget = {budget}, img_listing = {img_listing}, img_front = {img_front}, status = {status},
        #      price = {price}, date = {date} , property_title = {property_title},
        #      property_address = {property_address},  description = {description} , property_name = {property_name} ,
        #      home_area = {home_area}, rooms = {rooms}, baths = {baths},
        #      year_built = {year_built}, neigbourhood = {neigbourhood}, lot_dimensions={lot_dimensions},
        #      beds={beds},  balcony={balcony}, furnished={furnished}, completed={completed},
        #      living_room={living_room}, dining_area={dining_area}, garden={garden}, gym={gym}, img_gallery_1={img_gallery_1},
        #      img_gallery_2={img_gallery_2}, img_gallery_3={img_gallery_3}, air_conditioner={air_conditioner},     
        #      pool={pool}, wifi={wifi}, near_church={near_church}, near_estate={near_estate}, dish_washer={dish_washer}, security={security},
        #      indoor_game={indoor_game}, cable_tv={cable_tv}, microwave={microwave}
        #     ''') 
        property_id = generate_random_id()
        if param == 'house_for_sale':          
            a = HouseSale(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )            
            a.save()
            
        elif param == 'house_for_rent':    
            a = HouseRent(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )
            a.save()
        else:    
            a = HouseLease(property_id=property_id,location=location,
                          region=region,budget=budget,img_listing=img_listing,img_front=img_front,
                          status=status,price=price,date=date,property_title=property_title,property_address=property_address,description=description,
                          property_name=property_name,home_area=home_area,rooms=rooms,baths=baths,year_built=year_built,neigbourhood=neigbourhood,
                          lot_dimensions=lot_dimensions,beds=beds,balcony=balcony,furnished=furnished,completed=completed,living_room=living_room,
                          dining_area=dining_area,garden=garden,gym=gym,img_gallery_1=img_gallery_1,img_gallery_2=img_gallery_2,img_gallery_3=img_gallery_3,
                          air_conditioner=air_conditioner,pool=pool,wifi=wifi,near_church=near_church,near_estate=near_estate,dish_washer=dish_washer,
                          security=security,indoor_game=indoor_game,cable_tv=cable_tv,microwave=microwave,
                          )
            a.save()
        b = AllProperties(property_id = property_id , property_type=f'{param}', price=price, location=region, property_title = property_title)
        b.save()    


@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def add_property_house(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        # status_text = status.split('_')[1].capitalize()
        SaveFunction(request, status)
                                                                                                                                        
    #     region = request.POST.get('region')
    #     budget = request.POST.get('budget')
    #     file = request.POST.get('file')
    #     print(region, budget, file)
        # print('Posting')
    return render(request, 'admin-app/add-property_house.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def add_property_land(request):
    if request.method == "POST":
        property_id = generate_random_id()
        region = request.POST.get('region')
        location = request.POST.get('location')  
        property_title = request.POST.get('property_title') 
        budget = request.POST.get('budget') 
        img_listing = request.FILES.get('img_listing') 
        img_front = request.FILES.get('img_front') 
        date = request.POST.get('date') 
        property_address = request.POST.get('property_address') 
        price = request.POST.get('price') 
        property_name = request.POST.get('property_name')
        commercial = request.POST.get('commercial') == 'on' 
        serviced = request.POST.get('serviced') == 'on'
        fenced = request.POST.get('fenced') == 'on'
        water = request.POST.get('water') == 'on'
        electricity = request.POST.get('electricity') == 'on'
        plot_dimensions = request.POST.get('plot_dimensions')
        no_of_plots = request.POST.get('no_of_plots') 
        status = request.POST.get('status')
        description = request.POST.get('description') 
        # date_time = request.POST.get('date_time')
        video_land = request.FILES.get('video_land')
        video_thumbnail = request.FILES.get('video_thumbnail')
        # admin = request.POST.get('admin') 
        gps_address = request.POST.get('gps_address') 

        # print(f'''property_id = {property_id}, region ={region}, location={location}, property_title={property_title}, budget={budget},
        #       img_listing={img_listing}, img_front={img_front}, date={date}, property_address={property_address}, price={price},
        #        property_name={property_name}, commercial={commercial}, serviced={serviced}, fenced={fenced}, water={water}, electricity={electricity},
        #        plot_dimensions ={plot_dimensions}, no_of_plots={no_of_plots}, status={heyy}, description={description}, video_land={video_land},
        #        video_thumbnail ={video_thumbnail}, gps_address = {gps_address}
        #        ''')
        a = LandSale(property_id=property_id,region=region,location=location,property_title=property_title,budget=budget,img_listing=img_listing,img_front=img_front,
            date=date,property_address=property_address,price=price,property_name=property_name, commercial=commercial,serviced=serviced,fenced=fenced,water=water,electricity=electricity,
            plot_dimensions=plot_dimensions,no_of_plots=no_of_plots,status=status,description=description, video_land=video_land,video_thumbnail=video_thumbnail,gps_address=gps_address                  )
        a.save()
        b = AllProperties(property_id = property_id , property_type='land_for_sale', price=price, location=region)
        b.save()
    return render(request, 'admin-app/add-property_land.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def agent(request):
    return render(request, 'admin-app/agent.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def agent_invoice(request):
    return render(request, 'admin-app/agent-invoice.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def apartment(request):
    return render(request, 'admin-app/apartment.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blank(request):
    return render(request, 'admin-app/blank.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blog_dashboard(request):
    return render(request, 'admin-app/blog-dashboard.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blog_details(request):
    return render(request, 'admin-app/blog-details.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blog_grid(request):
    return render(request, 'admin-app/blog-grid.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blog_list(request):
    return render(request, 'admin-app/blog-list.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def blog_post(request):
    return render(request, 'admin-app/blog-post.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def chat(request):
    return render(request, 'admin-app/chat.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def contact(request):
    return render(request, 'admin-app/contact.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def events(request):
    return render(request, 'admin-app/events.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def file_dashboard(request):
    return render(request, 'admin-app/file-dashboard.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def file_documents(request):
    return render(request, 'admin-app/file-documents.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def file_images(request):
    return render(request, 'admin-app/file-images.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def file_media(request):
    return render(request, 'admin-app/file-media.html')


def forgot_password(request):
    return render(request, 'admin-app/forgot-password.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def image_gallery(request):
    return render(request, 'admin-app/image-gallery.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def invoices(request):
    return render(request, 'admin-app/invoices.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def locked(request):
    return render(request, 'admin-app/locked.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def mail_compose(request):
    return render(request, 'admin-app/mail-compose.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def mail_inbox(request):
    return render(request, 'admin-app/mail-inbox.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def mail_single(request):
    return render(request, 'admin-app/mail-single.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def map(request):
    return render(request, 'admin-app/map.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def office(request):
    return render(request, 'admin-app/office.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def page_offline(request):
    return render(request, 'admin-app/page-offline.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def pricing(request):
    return render(request, 'admin-app/pricing.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def profile(request):
    return render(request, 'admin-app/profile.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def property_detail(request):
    return render(request, 'admin-app/property-detail.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def property_list(request):
    return render(request, 'admin-app/property-list.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def property_list3(request):
    return render(request, 'admin-app/property-list3.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def property_list4(request):
    return render(request, 'admin-app/property-list4.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def reports(request):
    return render(request, 'admin-app/reports.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def search_results(request):
    return render(request, 'admin-app/search-results.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def shop(request):
    return render(request, 'admin-app/shop.html')


def sign_in(request):
    if request.method == "POST":
        print('Post start')
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                # if 'next=/admin-app' in request.get_full_path():
                view_name = request.get_full_path().split('next=/admin-app')[1][1:]
                if view_name == '':
                    return redirect(index)
                else:
                    # print(f"It is, {view_name}")
                    return redirect(view_name)
                # else:    
                #     return redirect(index)
            else:
                messages.error(request, "You are not an admin")
        else:
            messages.error(request, "Invalid Credentials")    
    logout(request)
    return render(request, 'admin-app/sign-in.html')


def sign_up(request):
    return render(request, 'admin-app/sign-up.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def timeline(request):
    return render(request, 'admin-app/timeline.html')


# def sign_up(request):
#     return render(request, 'admin-app/sign-up.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def villa(request):
    return render(request, 'admin-app/villa.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def widgets_app(request):
    return render(request, 'admin-app/widgets-app.html')

@user_passes_test(lambda u: u.is_staff, login_url='sign-in')
def widgets_data(request):
    return render(request, 'admin-app/widgets-data.html')
