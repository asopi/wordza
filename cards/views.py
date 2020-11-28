from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LearnSet
from .models import Vocabulary
from .forms import LanguageForm


@login_required
def learn_set_view(request):
    learn_set_list = LearnSet.objects.order_by('-creation_date')
    context = {
        "learn_sets": learn_set_list
    }
    return render(request, 'cards/learn_set_view.html', context)


@login_required
def create_view(request):
    language_form = LanguageForm()
    context = {
        "language_form": language_form
    }
    return render(request, 'cards/create_view.html', context)


@login_required
def learning_view(request, learn_set_id):
    learn_set = LearnSet.objects.get(pk=learn_set_id)
    context = {
        "learn_set": learn_set
    }
    return render(request, 'cards/learning_view.html', context)


@login_required
def progress_view(request, learn_set_id):
    learn_set = LearnSet.objects.get(pk=learn_set_id)
    context = {
        "learn_set": learn_set
    }
    return render(request, 'cards/progress_view.html', context)
