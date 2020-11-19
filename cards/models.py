from django.db import models

# Create your models here.


class LearnSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=9999)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

