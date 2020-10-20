from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import DetailView
import json
from .models import Hotel, Order

# Create your views here.


def hotel(request):
    context = {
        'hotels': Hotel.objects.all(),
        'title': 'Hotels'
    }
    return render(request, 'hotels.html', context)


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'readmore.html'


def checkout(request, pk):
    context = {
        'hotel': Hotel.objects.get(id=pk)
    }
    return render(request, 'checkout.html', context)


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    hotel = Hotel.objects.get(id=body['hotelId'])
    Order.objects.create(
        hotel=hotel
    )

    return JsonResponse('Payment completed!', safe=False)
