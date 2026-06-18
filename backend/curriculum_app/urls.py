"""App routes for the CRUD module."""
from django.urls import path

from . import views


app_name = "curriculum"

urlpatterns = [
    path("entries/", views.entry_list, name="entry_list"),
    path("entries/nuevo/", views.entry_create, name="entry_create"),
    path("entries/<int:pk>/editar/", views.entry_update, name="entry_update"),
    path("entries/<int:pk>/eliminar/", views.entry_delete, name="entry_delete"),
]
