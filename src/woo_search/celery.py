from celery import Celery

from woo_search.setup import setup_env

setup_env()

app = Celery("woo-search")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
