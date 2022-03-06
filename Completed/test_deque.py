from collections import deque
from functools import wraps
from time import time


def timing(f, N=1000):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        for _ in range(N):
            result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
            (f.__name__, args, kw, te-ts))
        return result
    return wrap

@timing
def sortedSquares_deque(nums: list[int]) -> list[int]:
    beg, end = 0, len(nums) - 1

    new = deque()
    while beg <= end:
        beg_num, end_num = nums[beg]**2, nums[end]**2
        if beg_num <= end_num:
            new.appendleft(end_num)
            end -= 1

        else:
            new.appendleft(beg_num)
            beg += 1

    return new

@timing
def sortedSquares_list(nums: list[int]) -> list[int]:
    beg = 0
    end = len(nums) - 1

    new = []
    while beg <= end:
        beg_num, end_num = nums[beg]**2, nums[end]**2
        if beg_num <= end_num:
            new.append(end_num)
            end -= 1

        else:
            new.append(beg_num)
            beg += 1

    return new[::-1]

start, end = -10000, 10000

sortedSquares_list(range(start, end))
sortedSquares_deque(range(start, end))