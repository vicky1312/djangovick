from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, date

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    Published_Date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
