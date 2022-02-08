def partition_cost(A, s1, s2, i, memo=None):
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


def partition(A):
    ''' Partition list A into two sublists where the difference of sums are minimum.
    '''
    memo = {}
    def dp(A, s1, s2, i, L1, L2):
        if i >= len(A):
            return (abs(s1 - s2), L1, L2)

        key = (i, s1)
        if key not in memo:
            case1, L11, L12 = dp(A, s1 + A[i], s2, i+1, L1+[A[i]], L2)
            case2, L21, L22 = dp(A, s1, s2 + A[i], i+1, L1, L2 + [A[i]])
            if case1 <= case2:
                memo[key] = (case1, L11, L12)
            else:
                memo[key] = (case2, L21, L22)
        return memo[key]
    return dp(A, 0, 0, 0, [], [])

if __name__ == "__main__":
    A = [5, 7, 2, 1, 10, 6, 8]
    print(partition(A))
