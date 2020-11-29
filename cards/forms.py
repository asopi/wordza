from django import forms
from .models import Vocabulary
from .models import LearnSet


class LanguageForm(forms.Form):
    source_language = forms.ChoiceField(choices=Vocabulary.language_choices)
    target_language = forms.ChoiceField(choices=Vocabulary.language_choices)


class LearnSetForm(forms.ModelForm):
    class Meta:
        model = LearnSet
        fields = ('name', 'description', 'vocabularies')
