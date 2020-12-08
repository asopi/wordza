from django import forms
from .models import Vocabulary


class VocabulariesForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ('title', 'description', 'language', 'target_language')
