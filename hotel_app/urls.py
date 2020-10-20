from django.urls import path
from .views import HotelDetailView, checkout
from . import views

urlpatterns = [
    path('hotel/', views.hotel, name='hotel'),

    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete"),
    path('detail/<int:pk>/', HotelDetailView.as_view(), name='detail'),

]
