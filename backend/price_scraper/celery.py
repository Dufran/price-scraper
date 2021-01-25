from celery import Celery
import os


from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "price_scraper.settings.production")
app = Celery("price_scraper")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
