from django.urls import path
from WebApp import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('Our_products/', views.all_products, name='Our_products'),
    path('filtered_products/<cat_name>/', views.filtered_products, name='filtered_products'),
    path('single_product/<int:p_id>/', views.single_product, name='single_product'),
    path('contact/', views.contact, name='contact'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('save_signup/', views.save_signup, name='save_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('cart/', views.cart, name='cart'),

]