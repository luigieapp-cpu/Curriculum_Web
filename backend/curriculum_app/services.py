"""Functional helpers that replace the original JavaScript render logic."""
from .models import CurriculumEntry


DEFAULT_SECTIONS = [
    {
        "anchor": "contacto",
        "title": "Contacto",
        "category": CurriculumEntry.CONTACT,
        "defaults": [
            {
                "title": "Luis Carlos Rodríguez",
                "subtitle": "Bogotá, Colombia | Email: luoffice@protonmail.com",
                "description": "",
                "link_label": "LinkedIn",
                "link_url": "https://www.linkedin.com/in/lucaro-1111-/",
            }
        ],
    },
    {
        "anchor": "perfil",
        "title": "Perfil",
        "category": CurriculumEntry.PROFILE,
        "defaults": [
            {
                "title": "Perfil profesional",
                "subtitle": "Servicios Profesionales | Experiencia del Cliente | Back Office",
                "description": "Análisis de datos, desarrollo de software, IA prompting, metodologias agiles y Power BI - Excel.",
                "link_label": "",
                "link_url": "",
            }
        ],
    },
    {
        "anchor": "educacion",
        "title": "Educacion",
        "category": CurriculumEntry.EDUCATION,
        "defaults": [
            {
                "title": "SENA",
                "subtitle": "Tecnologo en Analisis & Desarrollo Software (2025 - 2027)",
                "description": "",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "Universidad de San Buenaventura",
                "subtitle": "Diplomado en Analisis de Datos (2023)",
                "description": "",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "SENA",
                "subtitle": "Tecnico Bilingue en BPO (2019 - 2021)",
                "description": "",
                "link_label": "",
                "link_url": "",
            },
        ],
    },
    {
        "anchor": "experiencia",
        "title": "Experiencia laboral",
        "category": CurriculumEntry.EXPERIENCE,
        "defaults": [
            {
                "title": "NERDTEAM",
                "subtitle": "Tax Operations Specialist",
                "description": "Gestion de incorporacion de clientes, formularios fiscales (1065, 1120/5472), informes anuales y soporte tecnico sobre IRS.",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "CLARO INSURANCE",
                "subtitle": "Contract Specialist",
                "description": "Gestion de contratos en Salesforce, comunicacion con aseguradoras y proyectos internos en Click-Up.",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "ITERUM CONNECTIONS",
                "subtitle": "Bilingual Back-Office",
                "description": "Atencion a clientes de Perry Ellis International, gestion de pedidos y uso de Shopify y Kustomer CRM.",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "ATENTO",
                "subtitle": "Bilingual Back-Office",
                "description": "Soporte en Meta Business Suite y escalamiento de casos a soporte especializado.",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "SONDA",
                "subtitle": "Help-Desk Analyst",
                "description": "Resolucion de incidencias para Walmart Company usando Service Now y Jira.",
                "link_label": "",
                "link_url": "",
            },
            {
                "title": "MOZZART BET",
                "subtitle": "Soporte Mesa Ayuda",
                "description": "Atencion al cliente, supervision de la web y gestion de tickets en Jira.",
                "link_label": "",
                "link_url": "",
            },
        ],
    },
]


def serialize_entry(entry):
    return {
        "title": entry.title,
        "subtitle": entry.subtitle,
        "description": entry.description,
        "link_label": entry.link_label,
        "link_url": entry.link_url,
        "display_order": entry.display_order,
    }


def get_section_items(category, defaults):
    queryset = CurriculumEntry.objects.filter(category=category, is_active=True).order_by("display_order", "title")
    if queryset.exists():
        return [serialize_entry(entry) for entry in queryset]
    return defaults


def build_dashboard_context():
    sections = []
    for section in DEFAULT_SECTIONS:
        sections.append(
            {
                "anchor": section["anchor"],
                "title": section["title"],
                "items": get_section_items(section["category"], section["defaults"]),
            }
        )
    return {"sections": sections}
