from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reminders/details/(?P<id>.+?)/$', views.details, name='details'),
    url(r'^reminders/add_reminder$', views.add_reminder, name='add_reminder'),
]