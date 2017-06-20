from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Reminder

class ReminderListView(ListView):
    """Shows users a list of reminders"""

    model = Reminder


class ReminderDetailView(DetailView):
    """Shows users a single reminder"""

    model = Reminder


class ReminderCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new reminder"""

    model = Reminder

    fields = ['name', 'phone_number', 'time', 'description', 'time_zone']

    success_message = 'reminder successfully created.'


class ReminderUpdateView(SuccessMessageMixin, UpdateView):
    """Powers a form to edit existing reminders"""

    model = Reminder

    fields = ['name', 'phone_number', 'time', 'description', 'time_zone']

    success_message = 'reminder successfully updated.'


class ReminderDeleteView(DeleteView):
    """Prompts users to confirm deletion of an reminder"""

    model = Reminder
    success_url = reverse_lazy('list_reminders')
