from django.db import models

# Create your models here.


class FinancialNews(models.Model):
    url = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=500)
    source = models.CharField(max_length=50)
    pub_time = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.CharField(max_length=100)

