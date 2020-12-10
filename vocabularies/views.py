from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from google.cloud import translate_v2 as translate
from .forms import VocabulariesForm
from .models import Vocabulary
from .models import Vocable

translate_client = translate.Client()


@login_required
def vocabulary_view(request):
    """
    Takes request and returns rendered view for all vocabularies.
    In case of POST request, a new vocabulary is saved.
    """
    vocabularies = Vocabulary.objects.order_by('-creation_date')
    vocabulary_form = VocabulariesForm(request.POST or None)
    if request.method == 'POST' and vocabulary_form.is_valid():
        vocabulary_form.save()

    context = {
        "vocabulary_form": vocabulary_form,
        "languages": Vocabulary.language_choices,
        'vocabularies': vocabularies,
    }

    return render(request, "vocabularies/vocabulary_view.html", context)


@login_required
def edit_view(request, vocabulary_id):
    """
    Takes request and returns rendered view for editing the vocabulary and adding new words.
    """
    vocabulary = get_object_or_404(Vocabulary, pk=vocabulary_id)
    VocabularyFormSet = inlineformset_factory(
        Vocabulary, Vocable, fields=('value', 'translated_value'), extra=1)
    form = VocabulariesForm(instance=vocabulary)

    form_set = VocabularyFormSet(
        queryset=Vocable.objects.none(), instance=vocabulary)
    vocables = Vocable.objects.filter(vocabulary_id=vocabulary_id)

    if request.method == 'POST':
        form = VocabulariesForm(request.POST or None, instance=vocabulary)
        form_set = VocabularyFormSet(request.POST or None, instance=vocabulary)

        if form_set.is_valid() and form.is_valid():
            form.save()
            form_set.save()
            vocabulary = get_object_or_404(Vocabulary, pk=vocabulary_id)
            VocabularyFormSet = inlineformset_factory(
                Vocabulary, Vocable, fields=('value', 'translated_value'), extra=1)
            form_set = VocabularyFormSet(
                queryset=Vocable.objects.none(), instance=vocabulary)
            vocables = Vocable.objects.filter(
                vocabulary_id=vocabulary_id).order_by('-creation_date')
    context = {
        "form": form,
        "form_set": form_set,
        "vocables": vocables,
        "vocabulary": vocabulary
    }
    return render(request, "vocabularies/edit_view.html", context)


@login_required
def translate_vocable(request):
    """
    Takes the request including source language, target language and the word to be translated
    and sends it to Google Translate API.
    The response is the translated word which is returned.
    """
    if request.method == 'POST':
        value = request.POST["value"]
        language = request.POST["language"]
        target_language = request.POST["target_language"]
        response = translate_client.translate(
            value, source_language=language, target_language=target_language)
        return HttpResponse(response["translatedText"])
    else:
        return HttpResponse("")
