from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Beer, Award, Photo
from main_app import models
from .forms import DrinkingForm
import boto3
import uuid

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com'
BUCKET = 'beer-collector-swaroop'

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
    awards_beer_doesnt_have = Award.objects.exclude(id__in = beer.awards.all().values_list('id'))
    # instantiate the Drinking Form
    drinking_form = DrinkingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'drinking_form': drinking_form,
        'awards': awards_beer_doesnt_have
    })

def add_drinking(request, beer_id):
    # Create the model form using the data in the request.POST
    form = DrinkingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the beer_id assigned.
        # commit=False means we save it in memory, without actually storing in the db
        new_drinking = form.save(commit=False)
        new_drinking.beer_id = beer_id
        new_drinking.save()
    return redirect('detail', beer_id=beer_id)


def add_photo(request, beer_id):
    # photo-file will be the 'name' attribute on the <input type='file'>
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # the following key is to generate a unique key for s3, that will be appended to each img url
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build out the fill url string
            url = f'{S3_BASE_URL}/{BUCKET}/{key}'
            # assign photo to a beer_id or beer and save it to db
            photo = Photo(url=url, beer_id=beer_id)
            photo.save()
        except Exception as error:
            print('An error has occurred while uploading the file to S3');
            print(error)
    return redirect('detail', beer_id=beer_id)

def assoc_award(request, beer_id, award_id):
    Beer.objects.get(id=beer_id).awards.add(award_id)
    return redirect('detail', beer_id=beer_id)

def unassoc_award(request, beer_id, award_id):
    Beer.objects.get(id=beer_id).awards.remove(award_id)
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