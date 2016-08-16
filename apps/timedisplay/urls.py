from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
    url(r'^$', views.index),  #this matches the "/" pathway
    url(r'^users$', views.show)   #this matches the "/users" pathway
]
