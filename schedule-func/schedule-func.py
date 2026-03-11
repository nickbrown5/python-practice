import time
import sched

# Schedules a task to run at a specific time
def schedule_task(event_time, func, *args):
    """First attempt"""
    # current_time = time.time()
    # delay = event_time - current_time
    # if delay < 0:
    #     raise ValueError("Event time must be in the future.")
    
    # time.sleep(delay)
    # return func(*args)
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(event_time, 1, func, argument=args)
    print(f"{func.__name__}() scheduled to run at {time.ctime(event_time)}")
    scheduler.run()


if __name__ == "__main__":
    schedule_task(time.time() + 5, print, "Task executed after 5 seconds!", 'Done')
