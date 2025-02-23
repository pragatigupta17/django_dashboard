from django.urls import path 
from app import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('fee_details/',views.fee_details,name='fee_details'),
    path('student_details/',views.student_details,name='student_details'),
    path('fee_status/',views.fee_status,name='fee_status'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login')
]

     
     
    

