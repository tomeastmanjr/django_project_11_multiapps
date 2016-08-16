from django.shortcuts import render, HttpResponse, redirect
import random
import string

def index(request):
    if "count" not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
    "word":"".join(random.choice(string.ascii_uppercase + string.digits) for x in range(14))
    }
    return render(request, "rwg/index.html", context)

def show(request):
    print(request.method)
    return render(request, 'rwg/show_users.html')
