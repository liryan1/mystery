import numpy as np

def partition_cost(A: list) -> int:
    '''Returns the minimum difference of partitioning list A into two.
    No constraint on size of each list
    '''
    memo = {}
    def dp(A: list, s1: int, s2: int, i: int):
        if i >= len(A):
            return abs(s1 - s2)

        key = (i, s1)
        if key not in memo:
            case1 = dp(A, s1 + A[i], s2, i+1)
            case2 = dp(A, s1, s2 + A[i], i+1)
            memo[key] = min(case1, case2)
        return memo[key]
    return dp(A, 0, 0, 0)


def partition(A: list) -> tuple[int, list]:
    ''' Partition list A into two sublists where the difference of sums are minimum.
    Returns tuple of int: minimum difference of sums & list of elements in first list.
    '''
    memo = {}
    def dp(A, s1, s2, i, choice):
        if i >= len(A):
            return (abs(s1 - s2), choice)

        key = (i, s1)
        if key not in memo:
            case1, choice1 = dp(A, s1 + A[i], s2, i+1, choice + [A[i]])
            case2, choice2 = dp(A, s1, s2 + A[i], i+1, choice)
            if case1 <= case2:
                memo[key] = (case1, choice1)
            else:
                memo[key] = (case2, choice2)
        return memo[key]
    return dp(A, 0, 0, 0, [])


def partition_cost_bu(A:list) -> int:
    ''' Bottom up approach of partition_cost.
    '''
    m = sum(A)
    table = np.zeros((m, len(A)))
    table[A[0]-1, 0] = 1
    for i in range(1, len(A)):
        for j in range(m):
            if table[j, i-1]:
                table[j, i] = 1
                table[j+A[i]-1, i] = 1
    for j in range(m//2):
        if table[m//2+j, -1] or table[m//2-j, -1]:
            return j + m % 2
    return -1


if __name__ == "__main__":
    A = [5, 7, 2, 1, 10, 6, 8]
    print(partition_cost(A))
    print(partition_cost_bu(A))
