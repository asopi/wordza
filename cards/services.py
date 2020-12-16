from vocabularies.models import Vocabulary, Vocable
from .models import LearnSet

def calculate_progress(request, learn_set: LearnSet):
    """
    Takes a learn_set and calculates its progress by dividing
    all successfully learned Vocables with all Vocables.
    """
    vocables_count = 0
    successfull_learned = 0

    for vocabulary in learn_set.vocabularies.all():
        successfull_learned += Vocable.objects.filter(user=request.user, vocabulary_id=vocabulary.id, success_counter__gt = 0).count()
        vocables_count += Vocable.objects.filter(user=request.user, vocabulary_id=vocabulary.id).count()

        learn_set.progress = round(successfull_learned * 100 / vocables_count, 2)
    learn_set.save()
