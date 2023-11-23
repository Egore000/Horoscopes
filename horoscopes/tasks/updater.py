from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .parser import get_data

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data, 'interval', days=1)
    scheduler.start()