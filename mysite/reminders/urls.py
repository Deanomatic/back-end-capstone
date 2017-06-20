from django.conf.urls import url
 
from .views import ReminderListView, ReminderCreateView, ReminderDetailView, ReminderUpdateView, ReminderDeleteView

 

urlpatterns = [
    # List and detail views
    url(r'^list$', ReminderListView.as_view(), name='list_reminders'),

    url(r'^(?P<pk>[0-9]+)$', ReminderDetailView.as_view(), name='view_reminder'),

    # Create, update, delete
    url(r'^new$', ReminderCreateView.as_view(), name='new_reminder'),
    url(r'^(?P<pk>[0-9]+)/edit$', ReminderUpdateView.as_view(), name='edit_reminder'),
    url(r'^(?P<pk>[0-9]+)/delete$', ReminderDeleteView.as_view(), name='delete_reminder'),
]


