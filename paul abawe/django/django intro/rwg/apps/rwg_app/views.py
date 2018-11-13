from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['random'] = get_random_string(14)
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    
    return render(request, "index.html")

def generate(request):
    del request.session['attempt']
    return redirect('/')

def reset(request):
    del request.session['attempt']
    return redirect('/')