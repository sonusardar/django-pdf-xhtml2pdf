from django.db import models

# Create your models here.
class online_course(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    price = models.IntegerField()

