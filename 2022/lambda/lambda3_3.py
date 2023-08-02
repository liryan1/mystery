'''
Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
'''


from fractions import Fraction
from itertools import combinations
from functools import reduce
from math import gcd # if python 2.7, import it from fractions

def solution(m):
    stable = process(m)
    error, _sum, v0 = 1e-50, 0, [0]*len(m)
    v0[0] = 1
    for i in range(1000):
        v1 = multiply(m, v0)
        s = sum(abs(v1[i] - v0[i]) for i in range(len(v1)))
        if abs(_sum - s) < error:
            break
        _sum, v0 = s, v1

    # Get all values of stable states
    for i in range(len(stable)):
        stable[i] = v0[stable[i]].limit_denominator()
    
    return convert(stable)


def convert(stable):
    '''Convert fractions to integers and append denominator '''
    combs = combinations([x.denominator for x in stable], 2)
    denom = 1
    for item in combs:
        res = reduce(lcm, (a for a in item))
        denom = max(res, denom)

    answer = [(a * denom/a.denominator).numerator for a in stable]
    return answer + [denom]


def lcm(a, b):
    ''' Least common denominator for positive numbers a and b. '''
    return (a*b) // gcd(a, b)


def multiply(A, v):
    ''' Compute v*A
    '''
    n = len(v)
    res = [0]*n
    for i in range(n):
        for j in range(n):
            res[i] += A[j][i] * v[j]
    return res

def process(A):
    '''Change states to probabilities and end states to repeat itself. '''
    terminal = []
    for i in range(len(A)):
        _sum = sum(A[i])
        if _sum == 0:
            A[i][i] = Fraction(1, 1)
            terminal.append(i)
            continue
        for j in range(len(A[i])):
            A[i][j] = Fraction(A[i][j], _sum) # A[i][j]/_sum #
    return terminal
        

A = [
    # s0, the initial state, goes to s1 and s5 with equal probability
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]

B = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

print(solution(A))
print(solution(B))