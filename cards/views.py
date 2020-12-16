from random import shuffle
from distutils.util import strtobool
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vocabularies.models import Vocabulary, Vocable
from .models import LearnSet
from .forms import LanguageForm, LearnSetForm
from .services import calculate_progress

@login_required
def learn_set_view(request):
    """
    Takes request and returns the rendered view which displays the learn sets.
    In case of POST, the source and target language will be used to return a form for creating LearnSets
    which include Vocabularies in this language pair.
    The URL Parameter show_modal is used to let the view know that the Modal should be open for the LearnSet form.
    """
    learn_sets = LearnSet.objects.filter(user=request.user).order_by('-creation_date')
    language_form = LanguageForm()
    learn_set_form = LearnSetForm()
    if request.method == 'POST':
        language_form = LanguageForm(request.POST or None)
        learn_set_form = LearnSetForm(request.POST or None)
        if language_form.is_valid():
            learn_set_form = LearnSetForm()
            learn_set_form.fields["vocabularies"].queryset = Vocabulary.objects.filter(
                user=request.user,
                source_language=language_form.cleaned_data['source_language'],
                target_language=language_form.cleaned_data['target_language']
            )

        context = {
            "learn_sets": learn_sets,
            "learn_set_form": learn_set_form
        }

        return render(request, 'cards/learn_set_view.html', context)

    context = {
        "learn_sets": learn_sets,
        "language_form": language_form,
        "show_modal": request.GET.get('show-modal')
    }
    return render(request, 'cards/learn_set_view.html', context)


@login_required
def create_view(request):
    """
    Takes request and creates a LearnSet, after that the user is redirected to the LearnSet View.
    """
    if request.method == 'POST':
        learn_sets = LearnSet.objects.filter(user=request.user).order_by('-creation_date')
        learn_set_form = LearnSetForm(request.POST or None)
        if learn_set_form.is_valid():
            instance = learn_set_form.save(commit=False)
            instance.user = request.user
            learn_set_form.save()
            return redirect('cards:learn_set_view')
        else:
            context = {
                "learn_sets": learn_sets,
                "learn_set_form": learn_set_form
            }
            return render(request, 'cards/learn_set_view.html', context)


@login_required
def learning_view(request, learn_set_id):
    """
    Takes request and returns the rendered view with a shuffled List of Vocables which the user can learn.
    The Parameter learn_set_id is also taken to identify the LearnSet.
    """ 
    learn_set = LearnSet.objects.filter(user=request.user).get(pk=learn_set_id)
    vocables = []
    active_vocable = None

    for vocabulary in learn_set.vocabularies.all():
        vocables += Vocable.objects.filter(
                        user=request.user,
                        vocabulary_id=vocabulary.id,
                        success_counter=0)

    shuffle(vocables)

    if len(vocables) > 0:
        active_vocable = vocables[0]

    context = {
        "learn_set": learn_set,
        "vocables": vocables,
        "active_vocable": active_vocable
    }
    return render(request, 'cards/learning_view.html', context)

@login_required
def submit_vocable(request, learn_set_id, vocable_id):
    """
    Takes request and the parameter vocable_id to increase the succes or failed counter of a Vocable.
    """
    if request.method == 'POST':
        success = strtobool(request.POST["success"])
        learn_set = LearnSet.objects.filter(user=request.user).get(pk=learn_set_id)
        vocable = Vocable.objects.filter(user=request.user).get(pk=vocable_id)

        if success:
            vocable.success_counter += 1
        else:
             vocable.failed_counter += 1
        vocable.save()
        calculate_progress(request, learn_set)

    return redirect('/cards/learning/' + str(learn_set_id))


