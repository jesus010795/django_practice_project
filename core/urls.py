from django.urls import path
from . import views

# app_name = 'core_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    # path('contact/', views.contact, name='contact'),
    # path('sample/', views.sample, name='sample'),
]