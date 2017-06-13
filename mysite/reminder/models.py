from django.db import models
from datetime import datetime

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    reminder_time = models.IntegerField(null=True)
    time_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
    	return self.title

class User(models.Model):
	user_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)




# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)