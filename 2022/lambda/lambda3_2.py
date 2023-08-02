'''
Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same h - each step must be lower than the prev one. All steps must contain at least one brick. A step's h is classified as the total amount of b that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a h of 2 and the second step having a h of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given b. The two staircases can have hs (4, 1) or (3, 2)
'''

def dp(h, b, memo=None):
    ''' Dynamic programming solution with caching. 
        h: current height
        b: bricks left
    '''
    # Base cases:
    # (1) finished building, no b left
    if b == 0:
        return 1

    # (2) Not enough left to build more but did not use all b
    if b < h:
        return 0

    # Build h, look for higher, or don't build, look for higher
    if memo[h][b] < 0:
        memo[h][b] = dp(h + 1, b - h, memo) + dp(h + 1, b, memo)

    return memo[h][b]

def solution(n):
    memo = [[-1]*(n+1) for _ in range(n+1)]
    return dp(1, n, memo) - 1


if __name__ == "__main__":
    x = solution(10)
    print("answer:", x)