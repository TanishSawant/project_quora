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

print(User.first_name)