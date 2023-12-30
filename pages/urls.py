from django.urls import path
from . import views


urlpatterns = [
    path('', views.sample, name='sample'),
    path('pages/<int:page_id>/', views.category, name='page'),
    
    # path('',)
]