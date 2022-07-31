#========================================
# Scheduler Jobs
#========================================
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

# jobs
from todolist_app import views

scheduler.add_job(views.pdf, 'interval', seconds=86400)
scheduler.add_job(views.pdff, 'interval', seconds=86400)
scheduler.start()

#========================================86400