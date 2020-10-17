from django.urls import path
from .views import HotelDetailView
from . import views

urlpatterns = [
    path('hotel/', views.hotel, name='hotel'),

    path('detail/<int:pk>/', HotelDetailView.as_view(), name='detail'),

]
