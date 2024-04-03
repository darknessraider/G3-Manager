from django.contrib import admin
from home.models import Member
from partmanager.models import Subsystem, Part

# Register your models here.
admin.site.register(Member)
admin.site.register(Subsystem)
admin.site.register(Part)