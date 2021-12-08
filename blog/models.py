from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=250)
  date = models.DateField(default=datetime.now)

    #shows title in database
  def __str__(self):
    return self.title