#Periodic task
This task is used for calling api one time per a day.
I used Celery and django celery beat for it in my backend project.
#To run celery
Worker : celery -A currencyconverter worker -l info
Beat: celery -A currencyconverter beat - l info

Consider that Periodic task and its settings(about set interval, cron, scheduler and soon) are managed django admin panel

#Notes for Celery
You must use message broker (Rabbitmq, redis), I used Redis
Periodic Task must be always working.
Here, our periodic task is get_or_update.

This project is given me in interview when I join to startup, that's why, I firstly parse API and integrate to front(This process can be doing directly in front)  to show my skills over both of frontend and backend.

#Requirements install

pip install -r requirements.txt 
 
