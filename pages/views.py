from django.shortcuts import render

# Create your views here.\
from django.http import HttpResponse
import  django.template
from django.shortcuts import render

def index(request):
    return render(request, "pages/homepage.html", {})

def loginPage(request) :
    return render(request, "pages/login.html", {})

def signUpPage(request) :
    return render(request, "pages/SignUp.html", {})