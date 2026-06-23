#!/usr/bin/env python
"""Quick validation script for Django project."""
import os
import sys
import django

# Setup Django
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_web.settings")
django.setup()

from django.db import connection
from django.contrib.auth.models import User
from curriculum_app.models import CurriculumEntry

print("✓ Django initialized successfully")
print(f"✓ Database: {connection.settings_dict['ENGINE']}")

# Check migrations
from django.db.migrations.executor import MigrationExecutor
executor = MigrationExecutor(connection)
plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
if plan:
    print(f"⚠ Pending migrations: {len(plan)}")
else:
    print("✓ All migrations applied")

# Check users
users_count = User.objects.count()
print(f"✓ Users in database: {users_count}")

# Check curriculum entries
entries_count = CurriculumEntry.objects.count()
print(f"✓ Curriculum entries: {entries_count}")

print("\n✓ Project validation complete. Ready to run: python manage.py runserver")
