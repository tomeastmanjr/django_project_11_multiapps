from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = { "somekey":"somevalue" }
    return render(request, 'dis_ninjas/index.html', context)

def show(request):
    return render(request, 'dis_ninjas/show_ninjas.html')

def hide(request, color):
    if color == 'red' or color == 'orange' or color == 'blue' or color == 'purple':
            context = {
                "color": color
            }
    else:
        context = {
            "color": "mfapril"
        }
    return render(request, 'dis_ninjas/show_ninjas.html', context)
