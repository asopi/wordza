from django.contrib import admin

from .models import Vocable
from .models import Vocabulary

admin.site.register(Vocable)
admin.site.register(Vocabulary)
