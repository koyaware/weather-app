from django.urls import path
from . import views
from .views import remove_city

urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('delete/<str:city_name>/', remove_city, name='remove_city'),
]
