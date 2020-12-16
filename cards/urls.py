from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.learn_set_view, name='learn_set_view'),
    path('create/', views.create_view, name='create_view'),
    path('learning/<int:learn_set_id>/', views.learning_view, name='learning_view'),
    path('learning/submit/<int:learn_set_id>/<int:vocable_id>', views.submit_vocable, name='submit_vocable'),
]
