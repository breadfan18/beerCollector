from django.shortcuts import render

# Beer class
class Beer:
    def __init__(self, name, type, alcPercent, abuLevel, nationality):
        self.name = name
        self.type = type
        self.alcPercent = alcPercent
        self.abuLevel = abuLevel
        self.nationality = nationality

# Create some beers
beers = [
    Beer('Lagunitas', 'IPA', '7.6%', 8, 'India'),
    Beer('California Lager', 'Lager', '4.2%', 3, 'Germany'),
    Beer('Hefeweizen', 'Wheat', '5%', 4, 'Belgium')
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    return render(request, 'beers/index.html', {'beers': beers})