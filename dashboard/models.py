from django.db import models
from django.utils.translation import gettext_lazy as _


class Vocable(models.Model):

    class Language(models.TextChoices):
        GERMAN = 'DE', _('German')
        ENGLISH = 'EN', _('English')

    value = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENGLISH,
    )

    def __str__(self):
        return self.value


class Vocabulary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=9999)
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date modified')

    def __str__(self):
        return self.title
