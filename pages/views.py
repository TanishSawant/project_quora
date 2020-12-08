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
        print("HELLO")
        qs.append(tempObj(Question.objects.get(questionId = f'{question.id}'), question.to_dict()['score']))
        print("----------------------------------")
        print(question.id)
    context={
        'qs' : qs
    }
    return render(request, 'pages/solvedQuestionList.html', context)

def dashboardGraph(request):
    all_tests = Test.objects.all()
    total_tests = 0
    for test in all_tests:
        total_tests += 1
    all_questions = Question.objects.all()
    total_questions = 0
    for _ in all_questions:
        total_questions += 1
    all_questions = None
    ref = db.collection('user_data').document('userTanish1').collection('questions')
    questions = ref.stream()
    s = 0
    q = 0
    for question in questions:
        q += 1
        s += question.to_dict()['score']
    x_data = [x for x in range(1000)]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                        output_type='div')

    new_ref = db.collection('user_data').document('userTanish1').collection('test')
    tests = new_ref.stream()
    test_size = 0
    for test in tests:
        test_size += 1

    context = {
        'plot_div' : plot_div,
        'solvedQuestions' : q,
        'score' : s,
        'percent_score' : int(s/(4*q) * 100),
        'number_tests' : test_size,
        'percent_questions_solved' : int(q/total_questions * 100),
        'test_percentage' : int((test_size / total_tests) * 100)
    }
    return render(request, "pages/dashboard.html", context)


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