from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('questions/<str:subject>/<str:questionid>', views.displayQuestion, name = 'quiz/questions'),   
    path('questions/<str:questionId>/<str:score>', views.intermediate ,name='intermediate')
]