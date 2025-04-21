from django.db import models
class MyModel(models.Model):
  name = models.CharField(max_length=300)
  def __str__(self):
        return self.name

# Create your models here.
