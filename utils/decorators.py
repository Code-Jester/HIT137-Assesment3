import time
import functools

#simple decor for logging in
def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] Calling {func.__name__} with args={args[1:]}, kwargs={kwargs}')
        res = func(*args, **kwargs)
        print(f'[LOG] {func.__name__} returned type={type(res)}')
        return res
    return wrapper

#timer decoration
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        print(f'[TIMED] {func.__name__} took {(t1-t0):.3f}s')
        return res
    return wrapper

#decoration caching
def cached(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args[1:], tuple(sorted(kwargs.items())))
        if key in cache:
            print('[CACHE] Returning cached result')
            return cache[key]
        res = func(*args, **kwargs)
        cache[key] = res
        return res
    return wrapper

# combining the decorators
def timed_logged_cached(func):
    return logged(timed(cached(func)))

def log_and_time(func):
    return logged(timed(func))
