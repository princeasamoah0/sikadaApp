from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist_ajax', views.wishlist_Ajax, name='wishlist_ajax'),
    path('deleteWishlist_Ajax', views.deleteWishlist_Ajax, name='deleteWishlist_Ajax'),
    path('404', views.page_404, name='404'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('add-listing', views.add_listing, name='add-listing'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('blog-grid', views.blog_grid, name='blog-grid'),
    path('blog-left-sidebar', views.blog_left_sidebar, name='blog-left-sidebar'),
    path('blog-right-sidebar', views.blog_right_sidebar, name='blog-right-sidebar'),
    path('checkout/<str:property_id>', views.checkout, name='checkout'),
    path('blog', views.blog, name='blog'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('fetch-cart-items', views.fetch_cart_items, name='fetch-cart-items'),
    # path('check-duplicate-cart', views.check_duplicate_cart, name = 'check-duplicate-cart' ),
    path('delete-cart-item', views.delete_cart_item, name = 'delete-cart-item'),
    path('get-cart-count', views.get_cart_count, name = 'get-cart-count' ),
    path('cart', views.cart, name='cart'),
    path('coming-soon', views.coming_soon, name='coming-soon'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('history', views.history, name='history'),
    path('login', views.login_view, name='login'),
    path('logoutEvent', views.logoutEvent, name='logoutEvent'),
    path('locations', views.locations, name='locations'),
    path('order-tracking', views.order_tracking, name='order-tracking'),
    path('portfolio-2', views.portfolio_2, name='portfolio-2'),
    path('portfolio-details', views.portfolio_details, name='portfolio-details'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('product-details/<str:property_id>', views.product_details, name='product-details'),
    path('register', views.register, name='register'),
    path('service-details', views.service_details, name='service-details'),
    path('service', views.service, name='service'),
    path('shop-grid', views.shop_grid, name='shop-grid'),
    path('shop-left-sidebar', views.shop_left_sidebar, name='shop-left-sidebar'),
    path('shop-list', views.shop_list, name='shop-list'),
    path('shop-right-sidebar', views.shop_right_sidebar, name='shop-right-sidebar'),
    path('shop', views.shop, name='shop'),
    path('team-details', views.team_details, name='team-details'),
    path('team', views.team, name='team'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('land-details/<str:pk>', views.land_details, name='land-details'),
]
