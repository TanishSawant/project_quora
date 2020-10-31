from django.shortcuts import render
from django.http import HttpResponse
import  django.template
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from plotly.offline import plot
from plotly.graph_objs import Scatter
import quiz.tp as tp
from quiz.models import Question, Test

db = tp.getDb()

""" from firebase_admin import credentials
from firebase_admin import firestore """

def solvedQuestionsList(request):
    ref = db.collection('user_data').document('userTanish1').collection('questions')
    questions = ref.stream()
    qs = []
    class tempObj():
        def __init__(self, question, score):
            self.question = question
            self.score = score

    for question in questions:
        qs.append(tempObj(Question.objects.get(questionId = question.id), question.to_dict()['score']))
    context={
        'qs' : qs
    }       
    return render(request, 'pages/solvedQuestionList.html', context)

def dashboardGraph(request):
    x_data = [x for x in range(1000)]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                        output_type='div')
    return render(request, "pages/dashboard.html", context={'plot_div': plot_div})


def home(request):
    return render(request, "pages/homepage.html", {})

def loginPage(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request, f'Username and Password does not match')
    return render(request, "pages/login.html", {})

def signUpPage(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('Email')
        Password = request.POST.get('password')
        Confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(email = emailid).exists():
            messages.warning(request,"Email alreday exists!")

        elif User.objects.filter(username = username).exists():
            messages.warning(request, f'Username already exists!')

        if Password == Confirm_password:
            user = User.objects.create_user(username = username, password = Password, email = emailid)
            user.save()
            messages.success(request, f'User created with {username}')
            ref = db.collection('user_data').document(f'{username}')
            ref.set({
                'username' : username,
                'emailid' : emailid
            })
            return redirect('home')
    return render(request, "pages/SignUp.html", {})

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    return render(request,'pages/profile.html')