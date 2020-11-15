import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name___" took " str((end-start)*1000))
    return wrapper


def calc_square(nums):
    res = []
    for n in nums:
        res.append(n*n)
    return res

def calc_cube(nums):
    res = []
    for n in nums:
        res.append(n*n*n)
    return res

