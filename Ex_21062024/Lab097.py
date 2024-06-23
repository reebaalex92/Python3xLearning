
import time
def note_time_decorator(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print("Time taken", str(t2-t1))
    return wrapper()

@note_time_decorator
def log_function():
    time.sleep(5)
    print("The logs of time taken")


@note_time_decorator
def report_function():
    time.sleep(2)
    print("The logs of reporting time taken")

