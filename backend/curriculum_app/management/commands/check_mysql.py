"""Django management command to validate the MySQL/XAMPP connection."""
from django.core.management.base import BaseCommand, CommandError
from django.db import connections


class Command(BaseCommand):
    help = "Verifica la conexion a la base de datos configurada para XAMPP/MySQL."

    def handle(self, *args, **options):
        connection = connections["default"]
        try:
            connection.ensure_connection()
        except Exception as exc:  # pragma: no cover - surfaced in terminal
            raise CommandError(f"No se pudo conectar a la base de datos: {exc}") from exc

        self.stdout.write(self.style.SUCCESS("Conexion a MySQL/XAMPP verificada correctamente."))
