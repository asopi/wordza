from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9999)
    language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date modified')

    def __str__(self):
        return self.title


class Vocable(models.Model):
    value = models.CharField(max_length=200)
    translated_value = models.CharField(max_length=200)
    language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)
    creation_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value





