from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^show_ninjas$', views.show),
    url(r'^show_ninjas/(?P<color>[a-zA-Z]+)$', views.hide)
    ]
