from django.db import models
from home.models import Member

# Create your models here.
class Subsystem(models.Model):
    name = models.CharField(max_length=30)
    lead = models.ForeignKey(Member, on_delete=models.PROTECT, related_name = "lead")


class Part(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    creator = models.ForeignKey(Member, on_delete=models.PROTECT, related_name = "creator")
    builder = models.ForeignKey(Member, on_delete=models.PROTECT, related_name = "builder")

