from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import ManyToManyField
from simple_history.models import HistoricalRecords
from django.utils.html import mark_safe
import pandas as pd
from django.utils import timezone
from django.core.validators import MinValueValidator

from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email_users = models.ManyToManyField(User, related_name="email_users")

    def __str__(self):
        return self.phrase

class Item(models.Model):
    thread_id = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    text = models.TextField(max_length=1000)
    datetime = models.DateTimeField(blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title