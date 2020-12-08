from django.urls import path
from . import views

app_name = 'vocabularies'
urlpatterns = [
    path('', views.vocabulary_view, name="vocabulary_view"),
    path('vocabulary/<int:vocabulary_id>/', views.edit_view, name='edit_view'),
    path('translate/', views.translate_vocable, name='translate_vocable')
]
