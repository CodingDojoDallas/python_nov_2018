from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def Process(request):
    print("in process")
    if request.method == 'POST':
        if 'count' not in request.session:
            request.session['count'] = 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return redirect('/submit')

def Submit(request):
    return render(request, "results.html")

def Goback(request):
    request.session['count'] += 1
    return redirect('/')