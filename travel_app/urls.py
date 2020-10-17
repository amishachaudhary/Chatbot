from django.urls import path
from .views import PlaceDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),

    path('detail/<int:pk>/', PlaceDetailView.as_view(), name='detail'),
]
