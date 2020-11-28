from django import forms
from .models import Vocabulary


class LanguageForm(forms.Form):
    source_languages = forms.ChoiceField(choices=Vocabulary.language_choices)
    target_languages = forms.ChoiceField(choices=Vocabulary.language_choices)