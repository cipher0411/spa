# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import AccountView
from .views import view_appointments, appointment_success
from .views import login_view, logout_view, profile_view, appointment, user_appointment_view


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('price/', views.price, name='price'),
    path('gallery/', views.gallery, name='gallery'),
    path('appointment/', views.appointment, name='appointment'),
    path('404/', views.page_not_found, name='404'),
    # path('contact/', views.contact, name='contact'),
    path('cookies/', views.cookies, name='cookies'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
     path('appointment/', appointment, name='appointment'),
    path('appointment/success/', appointment_success, name='appointment_success'),
    path('appointments/', view_appointments, name='view_appointments'),
    path('account/', AccountView.as_view(), name='account'),
    path('contact/', views.contact_us, name='contact_us'),
    path('view-contacts/', views.view_contacts, name='view_contacts'),
     path('user_appointments/', user_appointment_view, name='user_appointment_view'),

]

