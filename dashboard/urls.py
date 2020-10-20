
from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('vocable/<int:vocable_id>/', views.detail, name='detail'),
    path('vocable/<int:vocable_id>/edit/',
         views.detail_edit, name='detail_edit'),
]
