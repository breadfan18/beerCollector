from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Beer, Award
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

def add_drinking(request, beer_id):
    # Create the model form using the data in the request.POST
    form = DrinkingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db unitl it has the beer_id assigned.
        # commit=False means we save it in memory, without actually storing in the db
        new_drinking = form.save(commit=False)
        new_drinking.beer_id = beer_id
        new_drinking.save()
    return redirect('detail', beer_id=beer_id)

class BeerCreate(CreateView):
    model = Beer
    fields = '__all__'

class BeerUpdate(UpdateView):
    model = Beer
    fields = ['type', 'alcPercent', 'abuLevel', 'origin']

class BeerDelete(DeleteView):
    model = Beer
    success_url = '/beers/'




class AwardList(ListView):
  model = Award

class AwardDetail(DetailView):
  model = Award

class AwardCreate(CreateView):
  model = Award
  fields = '__all__'

class AwardUpdate(UpdateView):
  model = Award
  fields = ['name', 'color']

class AwardDelete(DeleteView):
  model = Award
  success_url = '/awards/'