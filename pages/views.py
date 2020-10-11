from django.http import HttpResponse
import  django.template
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login


def index(request):
    return render(request, "/pages/homepage.html", {})

def loginPage(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user1 = User.authenticate(username = username, password = password)

        if user1 is not None:
            login(request, user1)
            return redirect('/pages/signup')
        else:
            messages.warning(request, f'Username and password does not match')
    
    return render(request, "pages/login.html", {})
    

def signUpPage(request) :

    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('Email')
        Password = request.POST.get('password')
        Confirm_password = request.POST.get('confirm_password')
        print(Password)
        print(Confirm_password)

        if username != None:

            if User.objects.filter(email = emailid).exists():
                messages.warning(request,"Email alreday exists!")
                
            elif User.objects.filter(user_name = username).exists():
                messages.warning(request, f'Username already exists!')
            
            if Password == Confirm_password:
                
                user = User.objects.create(user_name = username, password = Password, email = emailid)
                user.save()
                
                # messages.success(request, f'Account created with {username}')
                print('success of tatva')
                return redirect('/pages/login.html')
            else:
                messages.warning(request, f'Password and Confirm Password doesn\'t match!')

    return render(request, "/pages/SignUp.html")