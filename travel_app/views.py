from django.shortcuts import render
from django.views.generic import DetailView
from .models import Place

# Create your views here.
def home(request):
    context = {
        'places' : Place.objects.all()
    }
    return render(request, 'travel_app/index.html', context)

def about(request):
    return render(request, 'travel_app/about.html', {'title': 'About'})

def destination(request):
    context = {
        'places' : Place.objects.all(),
        'title': 'Destinations'
    }
    return render(request, 'travel_app/destination.html', context)

def contact(request):
    return render(request, 'travel_app/contact.html', {'title': 'Contact'})

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'travel_app/readmore.html'
