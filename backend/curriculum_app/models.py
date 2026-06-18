"""Database models for curriculum content."""
from django.db import models


class CurriculumEntry(models.Model):
    CONTACT = "contact"
    PROFILE = "profile"
    EDUCATION = "education"
    EXPERIENCE = "experience"

    CATEGORY_CHOICES = [
        (CONTACT, "Contacto"),
        (PROFILE, "Perfil"),
        (EDUCATION, "Educacion"),
        (EXPERIENCE, "Experiencia laboral"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=160, blank=True)
    description = models.TextField(blank=True)
    link_label = models.CharField(max_length=80, blank=True)
    link_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "display_order", "title"]

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"
