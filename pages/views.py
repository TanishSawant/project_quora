from django.shortcuts import render

# Create your views here.\
from django.http import HttpResponse
import  django.template
from django.shortcuts import render

def index(request):
    return render(request, "pages/index.html", {})
