from django.db import models

# Create your models here.

class Values(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    time = models.DateTimeField(default=None)
    value = models.PositiveBigIntegerField(default=None)
    
    