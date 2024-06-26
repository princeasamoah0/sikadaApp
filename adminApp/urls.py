from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.page_404, name='404'),
    path('500', views.page_500, name='500'),
    path('add-agent', views.add_agent, name='add-agent'),
    path('edit-add-property_house/<str:pk>', views.edit_add_property_house, name='edit-add-property_house'),
    path('add-property_house', views.add_property_house, name='add-property_house'),
    path('add-property_land', views.add_property_land, name='add-property_land'),
    path('agent', views.agent, name='agent'),
    path('agent-invoice', views.agent_invoice, name='agent-invoice'),
    path('apartment', views.apartment, name='apartment'),
    path('blank', views.blank, name='blank'),
    path('blog-dashboard', views.blog_dashboard, name='blog-dashboard'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('blog-grid', views.blog_grid, name='blog-grid'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-post', views.blog_post, name='blog-post'),
    path('chat', views.chat, name='chat'),
    path('contact', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('file-dashboard', views.file_dashboard, name='file-dashboard'),
    path('file-documents', views.file_documents, name='file-documents'),
    path('file-images', views.file_images, name='file-images'),
    path('file-media', views.file_media, name='file-media'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('image-gallery', views.image_gallery, name='image-gallery'),
    path('invoices', views.invoices, name='invoices'),
    path('locked', views.locked, name='locked'),
    path('mail-compose', views.mail_compose, name='mail-compose'),
    path('mail-inbox', views.mail_inbox, name='mail-inbox'),
    path('mail-single', views.mail_single, name='mail-single'),
    path('map', views.map, name='map'),
    path('office', views.office, name='office'),
    path('page-offline', views.page_offline, name='page-offline'),
    path('pricing', views.pricing, name='pricing'),
    path('profile', views.profile, name='profile'),
    path('property-detail/<str:pk>', views.property_detail, name='property-detail'),
    path('property-list', views.property_list, name='property-list'),
    path('property-list3', views.property_list3, name='property-list3'),
    path('property-list4', views.property_list4, name='property-list4'),
    path('reports', views.reports, name='reports'),
    path('search-results', views.search_results, name='search-results'),
    path('shop', views.shop, name='shop'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('timeline', views.timeline, name='timeline'),
    path('villa', views.villa, name='villa'),
    path('widgets-app', views.widgets_app, name='widgets-app'),
    path('widgets-data', views.widgets_data, name='widgets-data'),

]
