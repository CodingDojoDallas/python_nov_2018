from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

def index(request):
    context = {
        "time": strftime("%m-%d-%Y %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)
