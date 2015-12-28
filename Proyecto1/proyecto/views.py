from django.shortcuts import render
#from proyecto.models import *

def index(request):
    return render(request, 'index.html')
