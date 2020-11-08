from django.shortcuts import render
from .forms import VocabulariesForm
from django.contrib.auth.decorators import login_required


@login_required
def vocabulary_view(http_request, *args, **kwargs):
    # my_form = VocabulariesForm()
    # context = {
    #     "form": my_form
    # }
    return render(http_request, "vocabularies/vocabulary_view.html")


@login_required
def create_view(http_request, *args, **kwargs):
    return render(http_request, "vocabularies/create_view.html")
