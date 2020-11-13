from django import forms
from .models import Vocabulary


language_choices = (
    ('DE', 'German'),
    ('EN', 'English'),
    ('ES', 'Spanish'),
)

class VocabulariesForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=language_choices,
    )
    target_language = forms.ChoiceField(
        choices=language_choices,
    )
    class Meta:
        model = Vocabulary
        fields = ('title', 'description')

# class VocabulariesForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     language = forms.CharField(label='Select a language', widget=forms.Select(choices=language_choices))
#     target_language = forms.CharField(label='Select a language', widget=forms.Select(choices=target_language_choices))