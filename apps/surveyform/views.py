from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = { "somekey":"somevalue" }
    return render(request, "surveyform/index.html", context)

def result(request):
    context = request.session['context']
    del request.session['context']
    return render(request, 'surveyform/result.html', context)

def process(request):
    print(request.method)
    if "count" not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
    'name':request.POST['name'],
    'dojo':request.POST['dojo'],
    'favorite':request.POST['favorite'],
    'comment':request.POST['comment'] }
    request.session['context'] = context
    return redirect('/result')
