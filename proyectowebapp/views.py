from django.shortcuts import render
from carro.views import Carro

# Create your views here.
def home(request):
    carro = Carro(request) 
    return render(request, "proyectowebapp/home.html")

