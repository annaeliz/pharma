from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('login_admin',views.login_admin,name='login_admin'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('change_passworduser',views.change_passworduser,name='change_passworduser'),
    path('user_home',views.user_home,name='user_home'),
    path('my_orders', views.my_orders,name='my_orders'),
    path('product',views.product,name='product'),
    path('send_feedback', views.send_feedback,name='send_feedback'),
    path('view_feedback', views.view_feedback,name='view_feedback'),
    path('view_users',views.view_users,name='view_users'),
    path('view_booking',views.view_booking,name='view_booking'),
    path('update_orders/<int:pid>', views.update_orders,name='update_orders'),
    path('delete_order/<int:pid>', views.delete_order,name='delete_order'),
    path('delete_user/<int:pid>',views.delete_user,name='delete_user'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('view_product',views.view_product,name='view_product'),
    path('edit_product/<int:pid>',views.edit_product,name='edit_product'),
    path('delete_product/<int:pid>',views.delete_product,name='delete_product'),
    path('add_category',views.add_category,name='add_category'),
    path('view_category',views.view_category,name='view_category'),
    path('delete_category/<int:pid>',views.delete_category,name='delete_category'),
    path('categories',views.categories,name='categories'),
    path('Logout',views.Logout,name='Logout'),
    path('search', views.search_view,name='search'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('customer_address',views.customer_address,name='customer_address'),
    path('payment_success', views.payment_success,name='payment_success'),
    path('remove_from_cart/<int:pk>', views.remove_from_cart,name='remove_from_cart'),
    path('cat1',views.cat1,name='cat1'),
    path('cat2',views.cat2,name='cat2'),
    path('cat3',views.cat3,name='cat3'),
    path('cat4',views.cat4,name='cat4'),
    path('cat5',views.cat5,name='cat5'),
    path('cat6',views.cat6,name='cat6'),
    path('download/<int:orderID>/<int:productID>',views.download,name='download'),
    path('profile', views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()