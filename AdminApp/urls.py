from django.urls import path
from AdminApp import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),


    path('add_category/', views.add_category, name='add_category'),
    path('save_category',views.save_category,name='save_category'),
    path('view_category/', views.view_category, name='view_category'),
    path('edit_category/<int:c_id>/',views.edit_category,name='edit_category'),
    path('update_category/<int:c_id>/',views.update_category,name='update_category'),
    path('delete_category/<int:c_id>/',views.delete_category,name='delete_category'),


    path('add_products/', views.add_products, name='add_products'),
    path('save_products/', views.save_products, name='save_products'),
    path('view_products/', views.view_products, name='view_products'),
    path('edit_products/<int:p_id>/', views.edit_products, name='edit_products'),
    path('update_products/<int:p_id>/', views.update_products, name='update_products'),
    path('delete_products/<int:p_id>/', views.delete_products, name='delete_products'),

    path('add_services/', views.add_services, name='add_services'),
    path('save_services/', views.save_services, name='save_services'),
    path('view_services/', views.view_services, name='view_services'),
    path('delete_services/<int:s_id>/', views.delete_services, name='delete_services'),

    path('admin_login_page/', views.admin_login_page, name='admin_login_page'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('contact_data/', views.contact_data, name='contact_data'),

]