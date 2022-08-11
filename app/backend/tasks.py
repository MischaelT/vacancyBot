import schedule
import time

from backend.backend_manager import BackendManager

def job():
    backend_manager = BackendManager()
    backend_manager.run_general_parsing()

def initialise_sceduler():

    schedule.every().day.at("00:30").do(job)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)



