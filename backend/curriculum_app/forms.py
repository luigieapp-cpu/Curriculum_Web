"""Forms for login and CRUD operations."""
from django import forms

from .models import CurriculumEntry


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "usuario@ejemplo.com", "class": "input-field"}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": "Ingresa tu contraseña", "class": "input-field"}),
    )


class CurriculumEntryForm(forms.ModelForm):
    class Meta:
        model = CurriculumEntry
        fields = [
            "category",
            "title",
            "subtitle",
            "description",
            "link_label",
            "link_url",
            "display_order",
            "is_active",
        ]
        widgets = {
            "category": forms.Select(attrs={"class": "input-field"}),
            "title": forms.TextInput(attrs={"class": "input-field"}),
            "subtitle": forms.TextInput(attrs={"class": "input-field"}),
            "description": forms.Textarea(attrs={"class": "input-field", "rows": 5}),
            "link_label": forms.TextInput(attrs={"class": "input-field"}),
            "link_url": forms.URLInput(attrs={"class": "input-field"}),
            "display_order": forms.NumberInput(attrs={"class": "input-field", "min": 0}),
            "is_active": forms.CheckboxInput(attrs={"class": "checkbox-field"}),
        }
