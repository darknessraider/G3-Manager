from django.shortcuts import render
from partmanager.forms import PartRegisterForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpRequest
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
            Part(name=form.cleaned_data["part_name"], 
                 number=form.cleaned_data["part_number"], 
                 designer=member, 
                 priority=form.cleaned_data["priority"]).save()

            return HttpResponseRedirect("/")
        
    else:
        form = PartRegisterForm()

    return render(request, "registerpart.html", {"form": form})

def part_profile(request, id):
    part = Part.objects.get(id=id)
    return render(request, "part.html", {"part": part, "stagename": part.stages[part.stage]})


def electrical_review(request, id):
    return render(request, "partform.html")

def mentor_aproval(request, id):
    return HttpResponse("mentor_aproval")

def offical_release(request, id):
    return HttpResponse("offical_release")

def manufacturing(request, id):
    return HttpResponse("manufacturing")

def quality_control(request, id):
    return HttpResponse("quality_control")

def assembly(request, id):
    return HttpResponse("assembly")


def part_form(request, id, stage):
    views = {
        Part.Stage.ELECTRICAL_REVIEW: electrical_review,
        Part.Stage.MENTOR_APROVAL: mentor_aproval,
        Part.Stage.OFFICIAL_RELEASE: offical_release,
        Part.Stage.MANUFACTURING: manufacturing,
        Part.Stage.QUALITY_CONTROL: quality_control,
        Part.Stage.ASSEMBLY: assembly,
    }

    return views[stage](request, id)