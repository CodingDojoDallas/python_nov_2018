from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "date": datetime.today().strftime("%b %d, %Y"),
        'time': datetime.today().strftime("%H:%M %p")
    }
    return render(request, "time_app/index.html", context)