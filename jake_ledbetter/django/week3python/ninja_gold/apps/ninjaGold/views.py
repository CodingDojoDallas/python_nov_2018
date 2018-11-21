from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold'] = int(0)
    if 'actions' not in request.session:
        request.session['actions']= []

    request.session['house'] = int(random.randrange(2,6)),
    request.session['cave'] = random.randrange(5,11),
    request.session['farm'] = random.randrange(10,21),
    request.session['casino'] = random.randrange(-50,51)

    return render(request,'ninjaGold/index.html')

def process(request):
    print("beeeeeeeeeeeeforrreee")
    if request.POST['option'] == 'house':
        Inc = random.randrange(2,6)
        request.session['totalGold'] += Inc
    if request.POST['option'] == 'cave':
        Inc = random.randrange(5,11)
        request.session['totalGold'] +=Inc
    if request.POST['option'] == 'farm':
        Inc = random.randrange(10,21)
        request.session['totalGold'] += Inc
    if request.POST['option'] == 'casino':
        Inc = random.randrange(-50,51)
        request.session['totalGold'] += Inc
    temp = request.session['actions']
    if Inc > 0:
        temp.append({'text': "Earned " + str(Inc) + " gold from the " + request.POST["option"] + " At " + str(datetime.now()), 'color':'green'})
    if Inc < 0:
        temp.append({'text': "Lost " + str(Inc) + " gold from the " + request.POST["option"] + " At " + str(datetime.now()), 'color':'red'})
    request.session['actions'] = temp
    return redirect('/')
