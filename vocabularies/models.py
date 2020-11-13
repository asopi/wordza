from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9999)
    language = models.ChoiceField(max_length=2)
    target_language = models.ChoiceField(max_length=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Vocable(models.Model):
    value = models.CharField(max_length=200)
    translated_value = models.CharField(max_length=200)
    language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value





