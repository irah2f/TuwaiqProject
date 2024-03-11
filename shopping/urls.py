
from django.contrib import admin
from django.urls import path
from phone import views as v1 
from home import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v1.index, name='index'),
    path('showphone/', v1.showphone, name='showphone'),
    path('details/<int:id>/', v1.details, name='details'),
    path('auth_register/', v1.auth_register, name= 'auth_register'),
    path('auth_login/', v1.auth_login, name= 'auth_login'),
    path('auth_logout/', v1.auth_logout, name= 'auth_logout'),
    path('hometools/', v2.hometools, name='hometools'),
    path('checkout/<int:id>/', v1.checkout, name='checkout'),
    path('add_to_cart/<int:id>/', v1.add_to_cart, name='add_to_cart'),
    path('Homedetails/<int:id>/', v2.Homedetails, name='Homedetails'),
    path('HomeCheckout/<int:id>/', v2.HomeCheckout, name='HomeCheckout'),
    path('add_to_homecart/<int:id>/', v2.add_to_homecart, name='add_to_homecart'),
]
