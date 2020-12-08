from .models import Question

question = Question.objects.create(statement = "What are x-rays?", optionA = "X-rays", optionB = "I don't know", otionC = "You tell me", optionD = "ok")
