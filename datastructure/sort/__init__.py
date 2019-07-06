import time


def time_cost(func):
    def wrapper(*args, **kwargs):
        sTime = time.time()
        func(*args, **kwargs)
        print("Time cost:%s" % (time.time() - sTime))
    return wrapper

