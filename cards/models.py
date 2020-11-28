from django.db import models
from vocabularies.models import Vocabulary

# Create your models here.


class LearnSet(models.Model):
    name = models.CharField(max_length=200)
    vocabularies = models.ManyToManyField(Vocabulary)
    description = models.CharField(max_length=9999)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cards(models.Model):
    learn_set = models.ForeignKey(LearnSet, on_delete=models.CASCADE)
    front_side = models.CharField(max_length=200)
    back_side = models.CharField(max_length=200)
    success_counter = models.IntegerField()
    failed_counter = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.front_side

