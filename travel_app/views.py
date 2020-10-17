from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from .models import Place

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        print("Logged in")
    else:
        print("Not logged in")


def home(request):
    context = {
        'places': Place.objects.all()
    }
    return render(request, 'travel_app/index.html', context)


def about(request):
    return render(request, 'travel_app/about.html', {'title': 'About'})


def destination(request):
    context = {
        'places': Place.objects.all(),
        'title': 'Destinations'
    }
    return render(request, 'travel_app/destination.html', context)


def contact(request):
    return render(request, 'travel_app/contact.html', {'title': 'Contact'})


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'travel_app/readmore.html'


def search(request):
    query = request.GET['query']
    context = {
        'places': Place.objects.filter(title__icontains=query),

    }
    return render(request, 'travel_app/search.html', context)
