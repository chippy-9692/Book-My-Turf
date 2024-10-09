from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
   path('turf/',views.turf,name="turf"),
   path('about/',views.about,name="about"),
   path('check_availability/', views.check_availability, name='check_availability'),
    path('contactus/',views.contactus,name="contactus"),
   
]


