from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, "registerpart.html")

def build(request):
    return render(request, "buildpart.html")