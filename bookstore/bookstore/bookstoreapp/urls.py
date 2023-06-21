from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('reg_form', views.reg_form, name='reg_form'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]