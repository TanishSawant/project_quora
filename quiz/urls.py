from django.urls import path, include
from . import views

urlpatterns = [
    path('startQuiz/<str:id>', views.quiz, name='quiz'),
    path('questions/<str:subject>/<str:questionid>', views.displayQuestion, name = 'quiz/questions'),   
    path('questions123/<str:option>/<str:questionId>', views.intermediate ,name='intermediate'),
    path('testList', views.testList ,name='testList'),
    path('solved/<str:questionid>', views.displayQuestionAlone ,name='displayQuestionAlone'),
    path('abcdQuestion', views.getRandomQuestion ,name='getRandomQuestion'),
]#ruo