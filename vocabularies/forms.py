from django import forms
from .models import Vocabulary
from .models import Vocable

class VocabulariesForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ('title', 'description', 'language', 'target_language')

class VocableForm(forms.ModelForm):
    class Meta:
        model = Vocable
        fields = ('value','translated_value')