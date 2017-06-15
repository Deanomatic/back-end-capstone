from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from twilio.rest import Client

import arrow

from .models import Reminder


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client()

@shared_task
def send_sms_reminder(reminder_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our reminder from the database
    try:
        reminder = Reminder.objects.get(pk=reminder_id)
    except Reminder.DoesNotExist:
        # The Reminderreminder we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    reminder_time = arrow.get(reminder.time, reminder.time_zone.zone)
    body = 'Hi {0}. You have an reminder coming up at {1}.'.format(
        reminder.name,
        reminder_time.format('h:mm a')
    )

    message = client.messages.create(
        body=body,
        to=reminder.phone_number,
        from_=settings.TWILIO_NUMBER,
    )
