from django import forms
from reminder.models import Reminder, User
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.Charfield(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "password", "email")
class ReminderForm(forms.ModelForm):
	
	class Meta:
		model = Reminder
		fields = ("title", "descrition", "reminder_time", "time_created")