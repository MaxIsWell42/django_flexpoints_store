from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms 
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100, default='Flex points')
    description = models.CharField(max_length=200, default="Some flex points to keep you safe, traveler")
    pub_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default = 0)
    users_purchased = models.ForeignKey(User, on_delete=models.CASCADE, default='None')
    is_available = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                        choices=((False, 'No'), (True, 'Yes')))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
        