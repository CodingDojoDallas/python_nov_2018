from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['randomString'] = get_random_string(14)
    if 'iteration' in request.session:
        request.session['iteration'] += 1
    else:
        request.session['iteration'] = 1
    return render(request, 'index.html')

def generate(request):
    if request.method == 'POST':
        return redirect('/')

def reset(request):
    request.session['iteration'] = 0
    return redirect('/')
