from django.contrib import admin

# Register your models here.
from .models import Test, Question, testScoreData

# Register your models here.
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(testScoreData)