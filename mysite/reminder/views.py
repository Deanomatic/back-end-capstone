from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Reminder

def index(request):
	reminder = Reminder.objects.all()[:10]
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
		title = request.POST['title']
		description = request.POST['description']
		print("\n\n\ntitle{}\n{}\n\n\n".format(title, description))

		reminder = Reminder(title=title, description=description)
		reminder.save()
		return redirect('/reminder')

	else:
		return render(request, 'add_reminder.html')