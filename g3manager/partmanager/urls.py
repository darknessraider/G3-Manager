from django.urls import path

from . import views

urlpatterns = [
    path("partregister", views.register, name="index"),
    path("partbuild", views.build, name="index"),
]