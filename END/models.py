from django.db import models

# Create your models here.
class shan01(models.Model):
    col =models.CharField(max_length=10)
    

class she(models.Model):
    us =models.CharField(max_length=10)
    pwd =models.CharField(max_length=10)

    def __str__(self):
        return self.us



