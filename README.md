# Curriculum Web VS2

Proyecto web de currículum con Django y CRUD para administrar el contenido. La estructura quedó separada en:

- `backend/` para toda la parte Python/Django
- `frontend/` para plantillas HTML y estilos
- `db.sqlite3` como base local de desarrollo

## Estructura principal

- `backend/manage.py`
- `backend/curriculum_web/`
- `backend/curriculum_app/`
- `frontend/`

## Requisitos

- Python 3.14+
- Django instalado
- MySQL/MariaDB si vas a usar XAMPP

## Ejecución local

1. Instala dependencias:

```bash
pip install -r requirements.txt
```

2. Aplica migraciones:

```bash
python manage.py migrate
```

3. Ejecuta el servidor:

```bash
python manage.py runserver
```

## Verificación de MySQL/XAMPP

Si quieres validar la conexión con la base configurada, usa:

```bash
python backend/manage.py check_mysql
```

## Variables de entorno para MySQL

- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_HOST`
- `MYSQL_PORT`
