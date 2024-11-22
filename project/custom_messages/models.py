from importlib.metadata import requires

from django.db import models
from django.contrib.auth import get_user_model
import datetime
import jdatetime

user = get_user_model()

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(user, on_delete=models.CASCADE)
    # Get current Gregorian date
    gregorian_date = datetime.datetime.now()
    # Convert to Shamsi date
    shamsi_date = jdatetime.datetime.fromgregorian(date=gregorian_date.date()).date()
    is_approved = models.BooleanField(default=False)

