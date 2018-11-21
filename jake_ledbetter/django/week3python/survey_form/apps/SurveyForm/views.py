from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'SurveyForm/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return redirect('/submit')

def submit(request):
    return render(request, "SurveyForm/result.html")
