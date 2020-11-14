from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cards.models import LearnSet


@login_required
def dashboard_view(request):
    learn_sets = LearnSet.objects.order_by('-creation_date')

    context = {
        'title': 'DASHBOARD',
        'learn_sets': learn_sets,
    }

    return render(request, 'dashboard/dashboard.html', context)
