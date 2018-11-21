from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    if 'Word' not in request.session:
        request.session['Word'] = [{"word": 'word', "datetime": str(datetime.now()), "color":"color", "size":"small"}]
        print(request.session['Word'])
    return render(request,'index.html')

def add(request):
    temp = request.session['Word']
    temp.append({"word": request.POST['word'],'datetime': str(datetime.now()),'color':request.POST['color'], 'size':request.POST['size']})
    request.session['Word'] = temp
    print(request.session['Word'])
    return redirect('/')

def clearSession(request):
    request.session.clear()
    return redirect('/')
