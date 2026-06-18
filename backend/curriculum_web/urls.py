"""Root URL configuration for Curriculum Web."""
from django.contrib import admin
from django.urls import include, path

from curriculum_app import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("admin/", admin.site.urls),
    path("crud/", include("curriculum_app.urls")),
]
