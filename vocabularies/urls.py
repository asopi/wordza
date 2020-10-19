from django.urls import path
from . import views

app_name = 'vocabularies'
urlpatterns = [
    path('', views.index, name='index'),
]
