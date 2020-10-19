from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Vocable
from django.urls import reverse


def index(request):
    latest_vocable_list = Vocable.objects.order_by('-creation_date')[:5]

    context = {'latest_vocable_list': latest_vocable_list}
    return render(request, 'dashboard/index.html', context)


def detail(request, vocable_id):
    vocable = get_object_or_404(Vocable, pk=vocable_id)
    return render(request, 'dashboard/details.html', {'vocable': vocable})


def detail_edit(request, vocable_id):
    vocable = get_object_or_404(Vocable, pk=vocable_id)
    try:
        selected_language = vocable.language.get(pk=request.POST['language'])
    except (KeyError, Language.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'dashboard/detail.html', {
            'vocable': vocable,
            'languages': Vocable.Language.choices,
            'error_message': "You didn't select a language.",
        })
    else:
        selected_language.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('index:', args=(vocable.id,)))
