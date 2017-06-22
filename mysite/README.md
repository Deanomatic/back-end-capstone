# Memento
### A web application to keep all your reminders for yourself and others in one place.
---
# Installations and other requirements for running the app
* First fork this project to your repo and then clone it down to your machine.
* This project requires quite a few outside sources. Run all of the following commands in your command line to install all the dependancies though pip
    * `pip install celery`
    * `pip install twilio`
    * `pip install django-timezone-field`
    * `pip install celery[redis]`
    * `pip install arrow`
* Once the pip installs are done, your work of installations is complete.
* Start up your server by typing `python manage.py runserver`
* This app utilizes broker/message queue services called Celery and Redis
* In order for the reminders to actually be sent Celery must be running. To run Celery type `celery -A capstone.settings worker -l info`

Redis is not made for windows. So to get around this some seperate files were downloaded from a repo linked to the Redis site that makes Redis usable for windows. Click [here](https://github.com/MSOpenTech/redis) for details. This is not the conventional way to use Redis. If you are running a mac then the simple pip install above will work.

---
# Purpose of the app

> This is another way to help people keep track of their busy schedules. It provides a central place to keep track of everything. It also allows users to remind others of tasks at the chosen time. More are to be built out in this app in the future.    The frontend of this app uses django-material and takes advantage of the robust django admin.
