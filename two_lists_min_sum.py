def partition_cost(A: list, s1: int, s2: int, i: int, memo=None) -> int:
    '''Returns the minimum difference of partitioning list A into two.
    No constraint on size of each list
    '''
    if memo is None: memo = {}
    if i >= len(A):
        return abs(s1 - s2)

    key = (i, s1)
    if key not in memo:
        case1 = partition_cost(A, s1 + A[i], s2, i+1)
        case2 = partition_cost(A, s1, s2 + A[i], i+1)
        memo[key] = min(case1, case2)

    return memo[key]


def partition(A: list) -> tuple(int, list):
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

if __name__ == "__main__":
    A = [5, 7, 2, 1, 10, 6, 8]
    print(partition(A))
