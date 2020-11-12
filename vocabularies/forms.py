from django import forms

from .models import Vocabulary

language_choices = [
    ('German'),
    ('English'),
    ('Spanish'),
]

target_language_choices = [
    ('German'),
    ('English'),
    ('Spanish'),
]

class VocabulariesForm(forms.ModelForm):
    language = forms.CharField(label='Select a language', widget=forms.Select(choices=language_choices))
    target_language = forms.CharField(label='Select a language', widget=forms.Select(choices=target_language_choices))
    class Meta:
        model = Vocabulary
        fields = ('title', 'description', 'language', 'target_language')

# class VocabulariesForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     language = forms.CharField(label='Select a language', widget=forms.Select(choices=language_choices))
#     target_language = forms.CharField(label='Select a language', widget=forms.Select(choices=target_language_choices))