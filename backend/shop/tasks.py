from celery import shared_task
import requests
import json
from shop.models import *
from django.core import management
from django.conf import settings
from django.db import connections
from shop.spider import *
from shop.myspider import *


@shared_task
def cleanup():
    try:

        """Cleanup expired sessions by using Django management command."""
        management.call_command("clearsessions", verbosity=0)
        management.call_command("clean_duplicate_history", "--auto")
        # PUT MANAGEMENT COMMAND HERE
        return "success"
    except Exception as e:
        print(e)


@shared_task
def add(x, y):
    return x + y


@shared_task
def scra():
    result_queue = Queue()
    crawler = CrawlerWorker(MySpider(), result_queue)
    crawler.start()
    return "success"
