from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from ..loginreg.models import User

def index(request):
    context = {
        "courses":Course.objects.all(),
        "users": User.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    print(request.POST)
    Course.objects.create(name=request.POST["name"], description=request.POST["description"])
    return redirect('courses_index')

def delete(request, course_id):
    print(request.POST)
    course = Course.objects.get(id=course_id)
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, course_id):
	course = Course.objects.get(id=course_id)
	course.delete()
	return redirect("courses_index")

def users_courses(request):
    context = {
        "courses":Course.objects.all(),
        "users": User.objects.all()
    }
    print User.objects.all()
    return render(request, 'courses/users_courses.html', context)
