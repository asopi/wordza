from django.db import models
from django.contrib.auth.models import User
from vocabularies.models import Vocabulary


class LearnSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    vocabularies = models.ManyToManyField(Vocabulary)
    description = models.CharField(max_length=9999)
    progress = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


