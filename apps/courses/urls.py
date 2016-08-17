from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "courses_index"),
    url(r'^add$', views.add, name = "add"),
    url(r'^delete/(?P<course_id>\d+)$', views.delete, name = "delete"),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy, name = "destroy"),
    url(r'^users_courses$', views.users_courses, name = "users_courses"),
    url(r'^add_user$', views.add_user, name = "add_user"),

    ]
