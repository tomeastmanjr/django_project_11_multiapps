from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    context = { "somekey":"somevalue" }

    user = User.objects.all()
    print user
    return render(request, 'multiapps/index.html', context)

def show(request):
    print(request.method)
    return render(request, 'multiapps/show_users.html')
