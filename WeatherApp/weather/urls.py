from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('error/', views.error, name='error'),
    path('delete/<str:pk>/', views.deleteCity, name='delete')
]
