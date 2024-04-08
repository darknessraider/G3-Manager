from django.db import models
from home.models import Member

# Create your models here.
class Subsystem(models.Model):
    name = models.CharField(max_length=30)
    lead = models.ForeignKey(Member, on_delete=models.PROTECT, related_name = "lead")


class Part(models.Model):
    class Stage(models.IntegerChoices):
        ELECTRICAL_REVIEW = 1
        MENTOR_APROVAL = 2
        OFFICIAL_RELEASE = 3
        MANUFACTURING = 4
        QUALITY_CONTROL = 5
        ASSEMBLY = 6
        DONE = 7

    stages = {
        1: "Electrical Review",
        2: "Mentor Aproval",
        3: "Official Release",
        4: "Manufacturing",
        5: "Quality Control",
        6: "Assembly",
        7: "Done"
    }

    name = models.CharField(max_length=30)
    number = models.IntegerField()
    designer = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="designer")
    priority = models.IntegerField()
    stage = models.IntegerField(choices=Stage, default=Stage.ELECTRICAL_REVIEW)
    electrical_reviewer = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="electrical_reviewer", null=True)
