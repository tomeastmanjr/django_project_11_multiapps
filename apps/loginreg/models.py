from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from ..courses.models import Course
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')


class UserManager(models.Manager):
    def register(self, reg_data):
        first_name = reg_data['first_name']
        last_name = reg_data['last_name']
        email = reg_data['email']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(email=email)
        except:
            user = False
        if re.match("^[A-Za-z]+$", first_name) and re.match("^[A-Za-z]+$", last_name) and len(email) > 4 and EMAIL_REGEX.match(email) and len(password) >7 and password == confirm_password and not user:
            u = self.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
            print u
            print reg_data
            return (True,u)
        return (False,"this sucks")

    def login(self, log_data):
        email = log_data['email']
        user = self.filter(email=email)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or email are incorrect')



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # course = models.ForeignKey(Course, null=True)
    objects = UserManager()
