from http import server
from multiprocessing.managers import Server
from django.urls import path, include
from . import views


from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404



urlpatterns = [
    #path('singup/', views.Singup_view, name='singup'),
    path('', views.home, name='home'),
    path('page/', views.home_page),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('profile-edit/', views.profile_edit, name='profile-edit'),
    path('profile/', views.profile_view, name='profile'),
    path('view-profile/', views.view_profile, name='view-profile'),
    



  # This should work if django.contrib.auth.urls is correctly set up


    
    
    
    # Includes registration/account management

]

