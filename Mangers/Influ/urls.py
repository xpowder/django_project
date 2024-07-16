from django.urls import path
from . import views




urlpatterns = [
    #path('singup/', views.Singup_view, name='singup'),
    path('home/', views.home),
    path('page/', views.home_page),
    
    
    
    
    # Includes registration/account management

]

