from django.urls import path

from . import views

urlpatterns = [
    path("partregister", views.register, name="index"),
    path("part/<int:id>", views.part_profile, name="index"),
    path("part/<int:id>/<int:stage>", views.part_form, name="index"),
]