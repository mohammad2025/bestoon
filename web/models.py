from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expecse(models,Model):
    text = models.Charfield(max_length=255)
    date = models.DatesTimesFields()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
