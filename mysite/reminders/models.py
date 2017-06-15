from __future__ import unicode_literals

from reminder.settings import celery_app
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow


@python_2_unicode_compatible
class Reminder(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='US/Pacific')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'reminder #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('view_reminder', args=[str(self.id)])

    def clean(self):
        """Checks that reminders are not scheduled in the past"""

        reminder_time = arrow.get(self.time, self.time_zone.zone)

        if reminder_time < arrow.utcnow():
            raise ValidationError('You cannot schedule an reminder for the past. Please check your time and time_zone')

    def schedule_reminder(self):
        """Schedules a Celery task to send a reminder about this reminder"""

        # Calculate the correct time to send this reminder
        reminder_time = arrow.get(self.time, self.time_zone.zone)
        reminder_time = reminder_time.replace(minutes=-settings.REMINDER_TIME)

        # Schedule the Celery task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.apply_async((self.pk,), eta=reminder_time)

        return result.id

    def save(self, *args, **kwargs):
        """Custom save method which also schedules a reminder"""

        # Check if we have scheduled a reminder for this reminder before
        if self.task_id:
            # Revoke that task in case its time has changed
            celery_app.control.revoke(self.task_id)

        # Save our reminder, which populates self.pk,
        # which is used in schedule_reminder
        super(reminder, self).save(*args, **kwargs)

        # Schedule a new reminder task for this reminder
        self.task_id = self.schedule_reminder()

        # Save our reminder again, with the new task_id
        super(Reminder, self).save(*args, **kwargs)
