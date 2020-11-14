from django.shortcuts import render
from .forms import VocabulariesForm
from .forms import VocableForm
from django.contrib.auth.decorators import login_required
from .models import Vocabulary
from .models import Vocable


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

        context = {
            "form": voc_form,
            "message": "Successful!",
        }
        return render(request, "vocabularies/create_view.html", context)
    else:
        voc_form = VocabulariesForm()
        context = {
            "form": voc_form
        }
        return render(request, "vocabularies/create_view.html", context)

def index(request):
    latest_vocable_list = Vocabulary.objects.order_by('-creation_date')

    context = {'latest_vocabulary_list': latest_vocable_list}
    return render(request, 'vocabularies/vocabulary.html', context)



# def create_vocable_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         add_form = VocableForm(request.POST or None)
#
#         #add API
#         #add ID
#         if add_form.is_valid():
#             add_form.save()
#
#         context = {
#             "form": add_form,
#         }
#         return render(request, "vocabularies/create_view.html", context)