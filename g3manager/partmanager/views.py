from django.shortcuts import render
from partmanager.forms import PartRegisterForm
from django.http import HttpResponseRedirect
from home.models import Member
from partmanager.models import Part

# Create your views here.
def register(request):
    if request.method == "POST":
        form = PartRegisterForm(request.POST)
        if form.is_valid():
            if Member.objects.filter(name=form.cleaned_data["your_name"]).exists():
                member = Member.objects.get(name=form.cleaned_data["your_name"])
            else:
                member = Member(name=form.cleaned_data["your_name"])

            member.save()
            Part(name=form.cleaned_data["part_name"], number=form.cleaned_data["part_number"], creator=member, builder=None, finished=False, started=False).save()

            return HttpResponseRedirect("/")
        
    else:
        form = PartRegisterForm()

    return render(request, "registerpart.html", {"form": form})

def build(request):
    return render(request, "buildpart.html")