from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Product(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default = 0)

