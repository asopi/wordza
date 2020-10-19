from django.shortcuts import render


def index(request):
    return render(request, 'vocabularies/index.html')
