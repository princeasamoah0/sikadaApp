from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'admin-app/index.html')

def page_404(request):
    return render(request, 'admin-app/404.html')

def page_500(request):
    return render(request, 'admin-app/500.html')

def add_agent(request):
    return render(request, 'admin-app/add-agent.html')

def add_property(request):
    return render(request, 'admin-app/add-property.html')

def agent(request):
    return render(request, 'admin-app/agent.html')

def agent_invoice(request):
    return render(request, 'admin-app/agent-invoice.html')

def apartment(request):
    return render(request, 'admin-app/apartment.html')

def blank(request):
    return render(request, 'admin-app/blank.html')

def blog_dashboard(request):
    return render(request, 'admin-app/blog-dashboard.html')

def blog_details(request):
    return render(request, 'admin-app/blog-details.html')

def blog_grid(request):
    return render(request, 'admin-app/blog-grid.html')

def blog_list(request):
    return render(request, 'admin-app/blog-list.html')

def blog_post(request):
    return render(request, 'admin-app/blog-post.html')

def chat(request):
    return render(request, 'admin-app/chat.html')

def contact(request):
    return render(request, 'admin-app/contact.html')

def events(request):
    return render(request, 'admin-app/events.html')    

def file_dashboard(request):
    return render(request, 'admin-app/file-dashboard.html')

def file_documents(request):
    return render(request, 'admin-app/file-documents.html')

def file_images(request):
    return render(request, 'admin-app/file-images.html')  

def file_media(request):
    return render(request, 'admin-app/file-media.html') 

def forgot_password(request):
    return render(request, 'admin-app/forgot-password.html') 

def image_gallery(request):
    return render(request, 'admin-app/image-gallery.html') 

def invoices(request):
    return render(request, 'admin-app/invoices.html') 

def locked(request):
    return render(request, 'admin-app/locked.html') 

def mail_compose(request):
    return render(request, 'admin-app/mail-compose.html') 

def mail_inbox(request):
    return render(request, 'admin-app/mail-inbox.html')   

def mail_single(request):
    return render(request, 'admin-app/mail-single.html')  

def map(request):
    return render(request, 'admin-app/map.html')  

def office(request):
    return render(request, 'admin-app/office.html')  

def page_offline(request):
    return render(request, 'admin-app/page-offline.html')  

def pricing(request):
    return render(request, 'admin-app/pricing.html')  

def profile(request):
    return render(request, 'admin-app/profile.html')  

def property_detail(request):
    return render(request, 'admin-app/property-detail.html')  

def property_list(request):
    return render(request, 'admin-app/property-list.html')  

def property_list3(request):
    return render(request, 'admin-app/property-list3.html')  

def property_list4(request):
    return render(request, 'admin-app/property-list4.html')  

def reports(request):
    return render(request, 'admin-app/reports.html')  

def search_results(request):
    return render(request, 'admin-app/search-results.html')  

def shop(request):
    return render(request, 'admin-app/shop.html')  

def sign_in(request):
    return render(request, 'admin-app/sign-in.html')  

def sign_up(request):
    return render(request, 'admin-app/sign-up.html')  

def timeline(request):
    return render(request, 'admin-app/timeline.html')

def sign_up(request):
    return render(request, 'admin-app/sign-up.html')

def villa(request):
    return render(request, 'admin-app/villa.html')

def widgets_app(request):
    return render(request, 'admin-app/widgets-app.html')

def widgets_data(request):
    return render(request, 'admin-app/widgets-data.html')


