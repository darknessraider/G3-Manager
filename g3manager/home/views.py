from django.shortcuts import render
from django.http import HttpResponse
from partmanager.models import Part

# Create your views here.

def index(request):
    return render(request, "homepage.html", {'parts': Part.objects.all()})