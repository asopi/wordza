from django import forms
from .models import Vocabulary
from .models import LearnSet


class LanguageForm(forms.Form):
    source_language = forms.ChoiceField(
        choices=Vocabulary.language_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    target_language = forms.ChoiceField(
        choices=Vocabulary.language_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class LearnSetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vocabularies'].widget.attrs.update({'class': 'custom-select'})
    class Meta:
        model = LearnSet
        fields = ('title', 'description', 'vocabularies')
