"""Admin registration for curriculum models."""
from django.contrib import admin

from .models import CurriculumEntry


@admin.register(CurriculumEntry)
class CurriculumEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "display_order", "is_active", "updated_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "subtitle", "description")
    ordering = ("category", "display_order", "title")
