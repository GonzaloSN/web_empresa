from django.shortcuts import render
from .models import *

# Create your views here.

def services(request):
        services = Service.objects.all()
        return render(request, 'services/services.html', {'services':services})

def portfolio(request):
        projects = Project.objects.all()
        return render(request, 'portfolio/portfolio.html', {'projects':projects})