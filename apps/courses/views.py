from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Add_User
from ..loginreg.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse

def index(request):
    context = {
        "courses":Course.objects.all(),
        "users": User.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name=request.POST["name"], description=request.POST["description"])
    return redirect('courses_index')

def delete(request, course_id):
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
        "courses":Course.objects.annotate(user_count=Count("courses")),
        "users": User.objects.all()
    }
    return render(request, 'courses/users_courses.html', context)

def add_user(request):
    user_id = request.POST['userid']
    course_id = request.POST['courseid']
    user_list = User.objects.get(id=user_id)
    course_list = Course.objects.get(id=course_id)
    Add_User.objects.create(user=user_list, course=course_list)

    return redirect('users_courses')
