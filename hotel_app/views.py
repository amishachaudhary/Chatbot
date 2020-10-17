from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from .models import Hotel

# Create your views here.


def hotel(request):
    context = {
        'hotels': Hotel.objects.all(),
        'title': 'Hotels'
    }
    return render(request, 'hotels.html', context)


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel_app/hotels.html'
