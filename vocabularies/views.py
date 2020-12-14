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
    vocabularies = Vocabulary.objects.filter(user=request.user).order_by('-creation_date')
    vocabulary_form = VocabulariesForm(request.POST or None)
    if request.method == 'POST':
        if vocabulary_form.is_valid():
            instance = vocabulary_form.save(commit=False)
            instance.user = request.user
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
    vocables = Vocable.objects.filter(
        user=request.user,
        vocabulary_id=vocabulary_id
    ).order_by('-creation_date')
    vocabulary_form = VocabulariesForm(instance=vocabulary)
    
    VocabularyFormSet = inlineformset_factory(
        Vocabulary,
        Vocable,
        fields=('value', 'translated_value'),
        extra=1
    )
    form_set = VocabularyFormSet(
        queryset=Vocable.objects.none(),
        instance=vocabulary
    )

    if request.method == 'POST':
        vocabulary_form = VocabulariesForm(request.POST or None, instance=vocabulary)
        form_set = VocabularyFormSet(request.POST or None, instance=vocabulary)

        if form_set.is_valid():
            for form in form_set:
                instance_form = form.save(commit=False)
                instance_form.user = request.user
            form_set.save()
       
        if vocabulary_form.is_valid():
            instance_vocabulary_form = vocabulary_form.save(commit=False)
            instance_vocabulary_form.user = request.user
            vocabulary_form.save()


    context = {
        "vocabulary_form": vocabulary_form,
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
        source_language = request.POST["source_language"]
        target_language = request.POST["target_language"]
        response = translate_client.translate(
            value, source_language=source_language, target_language=target_language)
        return HttpResponse(response["translatedText"])
    else:
        return HttpResponse("")
