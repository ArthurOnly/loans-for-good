"""
This module is used to configure Celery for the project.
"""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loans_project.settings")

app = Celery("loans_project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
