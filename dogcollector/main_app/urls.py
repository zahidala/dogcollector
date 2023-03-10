from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>', views.dogs_detail, name='detail'),
    path('cats/create/', views.DogCreate.as_view(), name='dogs_create'),
]
