'''
Fibonacci sequence using log N runtime
fn+2 = fn+1 + fn
(fn+1, fn+2) = A*(fn, fn+1)
A = [
    0, 1
    1, 1
]

A^N
cache =[A, A^2, A^4, A^8]
A^11 = A^8 * A^2 * A

1011



log N time and space to generate cache
log N time to compute A^N

time: O(logN)
space: O(logN)
'''