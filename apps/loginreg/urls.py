from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "loginreg_index"),
    url(r'^register$', views.register, name = "register"),
    url(r'^login$', views.login, name = "login"),
    url(r'^reset$', views.reset, name = "reset")
    ]
