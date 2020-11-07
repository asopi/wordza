from django.shortcuts import render
from .forms import VocabulariesForm


def vocabulary_view(http_request, *args, **kwargs):
    # my_form = VocabulariesForm()
    # context = {
    #     "form": my_form
    # }
    return render(http_request, "vocabularies/vocabulary_view.html")

def create_view(http_request, *args, **kwargs):
    return render(http_request, "vocabularies/create_view.html")

