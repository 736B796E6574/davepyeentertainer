from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('contact', views.contact, name='contact'),  
    path('contact_confirmation', views.contact_confirmation, name='contact_confirmation'),  
]
