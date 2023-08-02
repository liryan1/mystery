def solution(l, t):
    ''' (list[int], int) -> [int, int]
    sum(0, j) - sum(0, i) = sum(i, j) = k
    '''
    presum = 0
    sums = {0:0} # sum(0, i): i
    for i in range(len(l)):
        presum += l[i]
        if presum - t in sums:
            return [sums[presum - t], i]
        sums[presum] = i + 1
    return [-1, -1]
