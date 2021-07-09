from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Beer
from main_app import models
from .forms import DrinkingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    beers = Beer.objects.all(); 
    return render(request, 'beers/index.html', {'beers': beers})

def beers_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    # instantiate the Drinking Form
    drinking_form = DrinkingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'drinking_form': drinking_form
    })

class BeerCreate(CreateView):
    model = Beer
    fields = '__all__'

class BeerUpdate(UpdateView):
    model = Beer
    fields = ['type', 'alcPercent', 'abuLevel', 'origin']

class BeerDelete(DeleteView):
    model = Beer
    success_url = '/beers/'