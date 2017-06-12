from django.http import HttpResponse
from django.shortcuts import render
from .models import Reminder

def index(request):
	reminder = Reminder.objects.all()[:5]
	context = {
		"reminders": reminder
	}
	return render(request, "index.html", context)

def details(request, id):
	reminder = Reminder.objects.get(pk=id)
	context = {
		"details": reminder
	}
	return render(request, "details.html", context)

def add_reminder(request):
	if(request.method == 'POST'):
		pass

	else:
		return render(request, 'add.html')