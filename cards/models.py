from django.db import models
from vocabularies.models import Vocabulary


class LearnSet(models.Model):
    name = models.CharField(max_length=200)
    vocabularies = models.ManyToManyField(Vocabulary)
    description = models.CharField(max_length=9999)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
