from django.shortcuts import render
from partmanager.forms import PartRegisterForm, ElectricalReviewForm
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


def add_stage_actor_to_part(part, stage, member):
    match stage:
        case Part.Stage.ELECTRICAL_REVIEW:
            part.electrical_reviewer = member


def part_form(request, id, stage):
    forms = {
        Part.Stage.ELECTRICAL_REVIEW: ElectricalReviewForm,
        #Part.Stage.MENTOR_APROVAL: mentor_aproval,
        #Part.Stage.OFFICIAL_RELEASE: offical_release,
        #Part.Stage.MANUFACTURING: manufacturing,
        #Part.Stage.QUALITY_CONTROL: quality_control,
        #Part.Stage.ASSEMBLY: assembly,
    }

    form = forms[stage]

    if request.method == "POST":
        form = ElectricalReviewForm(request.POST)
        if form.is_valid():
            if Member.objects.filter(name=form.cleaned_data["name"]).exists():
                member = Member.objects.get(name=form.cleaned_data["name"])

            member.save()
            part = Part.objects.get(id=id)
            part.stage += 1
            add_stage_actor_to_part(part, stage, member)
            part.save()

            return HttpResponseRedirect("/")
        
    else:
        form = ElectricalReviewForm()

    return render(request, "partform.html", {"form": form})