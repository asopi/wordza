from django.urls import path
from . import views

app_name = 'vocabularies'
urlpatterns = [
    path('', views.vocabulary_view, name="vocabulary_view"),
    path('vocabulary/<int:vocable_id>/', views.create_view, name='create_view'),
    path('create', views.create_view)
]

