from .forms import VocabulariesForm
from .forms import VocableForm
from django.contrib.auth.decorators import login_required
from .models import Vocabulary
from .models import Vocable
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.forms import inlineformset_factory
from google.cloud import translate_v2 as translate
from django.http import HttpResponse

translate_client = translate.Client()


@login_required
def vocabulary_view(request, *args, **kwargs):
    vocabularies = Vocabulary.objects.order_by('-creation_date')

    context = {
        'vocabularies': vocabularies,
    }

    return render(request, "vocabularies/vocabulary_view.html", context)


@login_required
def create_view(request, *args, **kwargs):
    if request.method == 'POST':
        voc_form = VocabulariesForm(request.POST or None)

        if voc_form.is_valid():
            voc_form.save()

        return vocabulary_view(request)
    else:
        voc_form = VocabulariesForm()
        context = {
            "form": voc_form
        }
        return render(request, "vocabularies/create_view.html", context)


@login_required
def translate_vocable(request):
    if request.method == 'POST':
        value = request.POST["value"]
        language = request.POST["language"]
        targed_language = request.POST["target_language"]
        response = translate_client.translate(
            value, source_language=language, target_language=targed_language)
        return HttpResponse(response["translatedText"])
    else:
        return HttpResponse("")


@login_required
def edit_view(request, vocabulary_id):
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
            vocables = Vocable.objects.filter(vocabulary_id=vocabulary_id).order_by('-creation_date')
            context = {
                "form": form,
                "form_set": form_set,
                "vocables": vocables,
                "vocabulary": vocabulary,
                "message": "Successful!",
            }
            return render(request, "vocabularies/edit_view.html", context)

    context = {
        "form": form,
        "form_set": form_set,
        "vocables": vocables,
        "vocabulary": vocabulary,
    }
    return render(request, "vocabularies/edit_view.html", context)
