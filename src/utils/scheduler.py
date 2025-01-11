from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

scheduler = BackgroundScheduler(
    jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')},
    executors={'default': ThreadPoolExecutor(10)},
    job_defaults={'coalesce': False, 'max_instances': 1}
)

def setup_scheduler(job_function):
    scheduler.add_job(
        job_function,
        trigger='interval',
        minutes=15,  # Adjust interval
        id='trading_workflow',
        replace_existing=True
    )
    return scheduler