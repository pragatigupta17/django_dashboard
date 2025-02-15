from django.urls import path 
from app import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login')
]

     
     
    

