from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reminders/details/(?P<id>.+?)/$', views.details, name='details'),
    url(r'^reminder/add_reminder$', views.add_reminder, name='add_reminder'),
    url(r'^reminder/edit_reminder/(?P<id>\d+)$', views.edit_reminder, name='edit_reminder'),
    url(r'^reminder/edit_reminder/update/(?P<id>\d+)$', views.update_reminder, name='update_reminder'),
    url(r'^reminder/delete_reminder/(?P<id>\d+)$', views.delete_reminder, name='delete_reminder'),
]