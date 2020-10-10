from django.shortcuts import render

# Create your views here.\
from django.http import HttpResponse
import  django.template
from django.shortcuts import render
from .models import User

def index(request):
    return render(request, "pages/homepage.html", {})

def loginPage(request) :
    return render(request, "pages/login.html", {})

def signUpPage(request) :
    print("--------------------------------------------------------")
    print(request.POST)
    print("-------------------------------------------")
    username = request.POST.get('username')
    emailid = request.POST.get('Email')
    Password = request.POST.get('password')
    User.objects.create(user_name = username, password = Password, email = emailid)
    return render(request, "pages/SignUp.html", {})