from __future__ import unicode_literals
from django.db import models
import datetime



class Posts(models.Model):
    """
        This is the Django database setup. 
        data available:
        title max_length 100
        description
        post_date
        image_name
        sale True/False
        featured True/False
        price
        temporary_price or sale price
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.DateTimeField('date published')
    image_name = models.CharField(max_length=50)
    sale = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    price = models.CharField(max_length=4)
    temporary_price = models.CharField(max_length=4)

    def __unicode__(self):
        return self.title
