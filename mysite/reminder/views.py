from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Reminder
import arrow

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
		reminder_time = request.POST['time']
		print("\n\n\ntitle{}\n{}\n\n\n".format(title, description))

		reminder = Reminder(title=title, description=description, reminder_time=reminder_time)
		reminder.save() 
		return redirect('/')

	else:
		return render(request, 'add_reminder.html')

def edit_reminder(request, id):
	reminder = Reminder.objects.get(pk=id)
	# print("\n\n\nHello again{}\n\n\n".format(reminder))
	context = {"reminder": reminder}
	return render(request, "edit_reminder.html", context)

def update_reminder(request, id):	
	reminder = Reminder.objects.get(pk=id)
	reminder.title = request.POST['title']
	reminder.description = request.POST['description'] 
	reminder.reminder_time = request.POST['time']
	print("\n\n\ntime{}\n\n\n".format(request.POST['time']))
	reminder.save()
	return redirect('/') 

def delete_reminder(request, id):
	reminder = Reminder.objects.get(pk=id)
	reminder.delete()
	return redirect('/')

def schedule_reminder():
	"""Schedules a Celery task to send a reminder about this appointment"""

	# Calculate the correct time to send this reminder
	appointment_time = arrow.get(reminder_time, time_zone.zone)
	reminder_time = appointment_time.replace(minutes=-settings.REMINDER_TIME)

	# Schedule the Celery task
	from .tasks import send_sms_reminder
	result = send_sms_reminder.apply_async((pk,), eta=reminder_time)

	return result.id