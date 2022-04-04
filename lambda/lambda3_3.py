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

def multiply(A, v):
    ''' Left Multiply state vector v by A, i.e. compute Av.
        A: list[list[int]] (n x n)
        v: list[int] nx1
    '''
    n = len(v)
    res = [0]*n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * v[j]
    return res


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

v0 = [1, 0, 0, 0, 0, 0]
v1 = multiply(A, v0)
for i in range(5):
    v0 = v1
    v1 = multiply(A, v0)
    print("time step:", i)
    print(v1)

