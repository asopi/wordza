from django import forms

class VocabulariesForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    creation_date = forms.DateTimeField()
    modification_date = forms.DateTimeField()
