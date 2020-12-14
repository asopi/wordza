from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cards.models import LearnSet
from vocabularies.models import Vocabulary, Vocable


@login_required
def dashboard_view(request):
    learn_sets = LearnSet.objects.filter(user=request.user).order_by('-creation_date')
    vocabularies = Vocabulary.objects.filter(user=request.user).order_by('-creation_date')
    vocables = Vocable.objects.filter(user=request.user).order_by('-creation_date')

    context = {
        'learn_sets': learn_sets,
        'vocabularies': vocabularies,
        'vocables': vocables,
    }

    return render(request, 'dashboard/dashboard.html', context)
