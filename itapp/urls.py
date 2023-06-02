from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('careers/',views.careers,name='careers'),
    path('quotes/',views.quotes,name='quotes'),
    path('servicedetails/',views.servicedetail,name='servicedetail'),
    path('jobdetails/',views.jobdetails,name='jobdetails'),
    path('gallery/',views.gallery,name='gallery')
    
    
    
    
]
