from django.contrib import admin

from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
	# list_filter = ('title', 'description')
	search_fields = ('title', 'description')

admin.site.register(Reminder, ReminderAdmin)