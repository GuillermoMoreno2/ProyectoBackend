from django.db import models
from datetime import datetime


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)
    date = models.DateField(default=datetime.today)

    def __str__(self) -> str:
        return self.title