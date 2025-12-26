from apscheduler.schedulers.background import BackgroundScheduler
from models import Session, Lead

def follow_up():
    db = Session()
    leads = db.query(Lead).filter(Lead.status == "new").all()
    for lead in leads:
        print(f"Follow-up reminder for {lead.email}")
    db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(follow_up, "interval", days=1)
    scheduler.start()
