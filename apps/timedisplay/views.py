from django.shortcuts import render, HttpResponse
import datetime
# now = datetime.datetime.now()
# Create your views here.
def index(request):
    # context = {
    # "time":now
    # }
    # # return render(request, 'timedisplay/index.html', context)
    return render(request, 'timedisplay/index.html', {"time":datetime.datetime.now()})

def show(request):
    print(request.method)
    return render(request, 'timedisplay/show_users.html')
