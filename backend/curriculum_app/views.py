"""Views for the curriculum dashboard and CRUD."""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CurriculumEntryForm, LoginForm
from .models import CurriculumEntry
from .services import build_dashboard_context


def home(request):
    context = build_dashboard_context()
    if request.user.is_authenticated:
        context["show_login"] = False
    else:
        context["show_login"] = True
        context["login_form"] = LoginForm()
    return render(request, "index.html", context)


def login_view(request):
    if request.method != "POST":
        return redirect("home")

    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sesion iniciada correctamente.")
            return redirect("home")
        form.add_error(None, "Email o contraseña incorrectos.")

    context = build_dashboard_context()
    context["show_login"] = True
    context["login_form"] = form
    return render(request, "index.html", context, status=400)


def logout_view(request):
    logout(request)
    messages.info(request, "Sesion cerrada.")
    return redirect("home")


@login_required
def entry_list(request):
    category_filter = request.GET.get("category", "")
    entries = CurriculumEntry.objects.all()

    if category_filter:
        entries = entries.filter(category=category_filter)

    return render(
        request,
        "entry_list.html",
        {
            "entries": entries.order_by("category", "display_order", "title"),
            "category_filter": category_filter,
            "category_choices": CurriculumEntry.CATEGORY_CHOICES,
        },
    )


@login_required
def entry_create(request):
    if request.method == "POST":
        form = CurriculumEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado correctamente.")
            return redirect("curriculum:entry_list")
    else:
        form = CurriculumEntryForm()

    return render(request, "entry_form.html", {"form": form, "title": "Nuevo registro"})


@login_required
def entry_update(request, pk):
    entry = get_object_or_404(CurriculumEntry, pk=pk)
    if request.method == "POST":
        form = CurriculumEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro actualizado correctamente.")
            return redirect("curriculum:entry_list")
    else:
        form = CurriculumEntryForm(instance=entry)

    return render(request, "entry_form.html", {"form": form, "title": "Editar registro"})


@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(CurriculumEntry, pk=pk)
    if request.method == "POST":
        entry.delete()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect("curriculum:entry_list")

    return render(request, "entry_confirm_delete.html", {"entry": entry})
