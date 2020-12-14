from django import forms
from .models import Vocabulary


class VocabulariesForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ('title', 'description', 'source_language', 'target_language')
