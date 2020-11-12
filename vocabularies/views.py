from django.shortcuts import render
from .forms import VocabulariesForm
from django.contrib.auth.decorators import login_required
from .models import Vocabulary

@login_required
def vocabulary_view(httprequest, *args, **kwargs):
    voc_form = VocabulariesForm(httprequest.POST or None)

    if voc_form.is_valid():
        voc_form.save()
        voc_form = VocabulariesForm()

    context = {
        "form": voc_form
    }
    return render(httprequest, "vocabularies/vocabulary_view.html", context)

# def vocabulary_view(httprequest, *args, **kwargs):
#         my_form = VocabulariesForm(httprequest.POST or None)
#         print(httprequest.POST)
#         if my_form.is_valid():
#             Vocabulary.objects.create(**my_form.cleaned_data)
#             my_form = VocabulariesForm()
#
#         context = {
#         "form": my_form
#         }
#         return render(httprequest, "vocabularies/vocabulary_view.html", context)


# if httprequest.method == "POST":
#     #print(httprequest.POST)
#     new_title = httprequest.POST.get('title')
#     new_description = httprequest.POST.get('description')
#     new_language = httprequest.POST.get('language')
#     new_target_language = httprequest.POST.get('target_language')
#
#     Vocabulary.objects.create(title=new_title,
#                               description=new_description,
#                               language=new_language,
#                               target_language=new_target_language)


@login_required
def create_view(request, *args, **kwargs):
    return render(request, "vocabularies/create_view.html")
