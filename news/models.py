from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=50)