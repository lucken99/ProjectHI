from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#writing first view

def index(request):
    return HttpResponse("Welcome to HI!")