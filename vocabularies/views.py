from .forms import VocabulariesForm
from .forms import VocableForm
from django.contrib.auth.decorators import login_required
from .models import Vocabulary
from .models import Vocable
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render


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


def edit_view(request, vocabulary_id):
    vocabulary = get_object_or_404(Vocabulary, pk=vocabulary_id)
    if request.method == 'POST':
        vocabulary_form = VocabulariesForm(request.POST or None, instance=vocabulary)
        vocable_form = VocableForm(request.POST or None)
        vocable_form.fields['vocabulary_id'] = vocabulary_id


        if vocabulary_form.is_valid():
            vocabulary_form.save()

        if vocable_form.is_valid():
            vocable_form.save()

        vocables = get_list_or_404(Vocable, vocabulary_id=vocabulary_id)

        context = {
            "vocabulary_form": vocabulary_form,
            "vocable_form": vocable_form,
            "vocables": vocables,
            "message": "Successful!",
        }
        return render(request, "vocabularies/edit_view.html", context)
    else:
        vocabulary_form = VocabulariesForm(instance=vocabulary)
        vocable_form = VocableForm()
        vocables = get_list_or_404(Vocable, vocabulary_id=vocabulary_id)

        context = {
            "vocabulary_form": vocabulary_form,
            "vocable_form": vocable_form,
            "vocables": vocables,
        }

        return render(request, 'vocabularies/edit_view.html', context)



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