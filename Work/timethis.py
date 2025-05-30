import time
def timethis(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end-start : 0.4f} secs")
        return res

    return wrapper



