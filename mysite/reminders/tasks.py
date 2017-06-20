# from __future__ import absolute_import


# from celery import shared_task
# from django.conf import settings
# from twilio.rest import Client

# import arrow
 
# from .reminders.models import Reminder


# TWILIO_ACCOUNT_SID = "AC4ddddb7fb7c8577e8aecee84587d1bd9"
# TWILIO_AUTH_TOKEN = "af02d291f7b9d55e762fcca4bf1e"
# # Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# # environment variables
# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# @shared_task
# def send_sms_reminder(reminder_id):
#     """Send a reminder to a phone using Twilio SMS"""
#     # Get our reminder from the database
#     try:
#         reminder = Reminder.objects.get(pk=reminder_id)
#     except Reminder.DoesNotExist:
#         # The Reminderreminder we were trying to remind someone about
#         # has been deleted, so we don't need to do anything
#         return

#     reminder_time = arrow.get(reminder.time, reminder.time_zone.zone)
#     body = 'Hi {0}. You have a reminder coming up at {1}.'.format(reminder.name,
#      reminder_time.format('h:mm a'))
 
#     message = client.messages.create(
        
#         body=body,
#         to=reminder.phone_number,
#         from_=settings.TWILIO_NUMBER,
#     )
