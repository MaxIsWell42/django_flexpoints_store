from django.db import models

class Product(models.Model):
    product_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date added')
    likes = models.IntegerField(default = 0)

