from __future__ import unicode_literals
from django.db import models
# from ..loginreg.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Add_User(models.Model):
	user = models.ForeignKey("loginreg.user", related_name="users")
	course = models.ForeignKey(Course, related_name="courses")
 	created_at = models.DateTimeField(auto_now_add = True)
 	updated_at = models.DateTimeField(auto_now = True)
