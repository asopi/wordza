from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LearnSet
from vocabularies.models import Vocabulary, Vocable
from .forms import LanguageForm, LearnSetForm


@login_required
def learn_set_view(request):
    learn_sets = LearnSet.objects.order_by('-creation_date')
    language_form = LanguageForm()
    learn_set_form = LearnSetForm()
    if request.method == 'POST':
        language_form = LanguageForm(request.POST or None)
        learn_set_form = LearnSetForm(request.POST or None)
        if language_form.is_valid():
            learn_set_form = LearnSetForm()
            learn_set_form.fields["vocabularies"].queryset = Vocabulary.objects.filter(
                language=language_form.cleaned_data['source_language']).filter(
                target_language=language_form.cleaned_data['target_language'])

        context = {
            "learn_sets": learn_sets,
            "learn_set_form": learn_set_form
        }
        return render(request, 'cards/learn_set_view.html', context)

    elif learn_set_form.is_valid():
        learn_set_form.save()

    context = {
        "learn_sets": learn_sets,
        "language_form": language_form,
        "show_modal": request.GET.get('show-modal')
    }
    return render(request, 'cards/learn_set_view.html', context)


@login_required
def create_view(request):
    learn_sets = LearnSet.objects.order_by('-creation_date')
    if request.method == 'POST':
        learn_set_form = LearnSetForm(request.POST or None)
        if learn_set_form.is_valid():
            learn_set_form.save()
        else:
            context = {
                "learn_sets": learn_sets,
                "learn_set_form": learn_set_form
            }
            return render(request, 'cards/learn_set_view.html', context)

    return redirect('cards:learn_set_view')


@login_required
def learning_view(request, learn_set_id):
    learn_set = LearnSet.objects.get(pk=learn_set_id)
    vocables = []
    for vocabulary in learn_set.vocabularies.all():
        vocables += Vocable.objects.filter(
            vocabulary_id=vocabulary.id)
    context = {
        "learn_set": learn_set,
        "vocables": vocables
    }
    return render(request, 'cards/learning_view.html', context)


@login_required
def progress_view(request, learn_set_id):
    learn_set = LearnSet.objects.get(pk=learn_set_id)
    context = {
        "learn_set": learn_set
    }
    return render(request, 'cards/progress_view.html', context)
