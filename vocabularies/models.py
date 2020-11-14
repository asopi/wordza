from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9999)
    language_choices = (
        ('DE', 'German'),
        ('EN', 'English'),
        ('ES', 'Spanish'),
    )
    language = models.CharField(max_length=2, choices=language_choices)
    target_language = models.CharField(max_length=2, choices=language_choices)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Vocable(models.Model):
    vocabulary_id = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    translated_value = models.CharField(max_length=200)
    language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value





