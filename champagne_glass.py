def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    ''' After pouring some non-negative integer cups of champagne in a champagne tower, return how full the jth glass in the ith row is (both i and j are 0-indexed.)
    '''
    # math solution didn't work. Ended up doing a top down DP
    glasses = [[0]*101 for _ in range(101)]
    glasses[0][0] = poured
    for row in range(100):
        for col in range(100):
            if glasses[row][col] > 1:
                # pour evenly into lower glasses
                glasses[row+1][col] += (glasses[row][col] - 1) / 2
                glasses[row+1][col+1] += (glasses[row][col] - 1) / 2
                glasses[row][col] = 1
    return glasses[query_row][query_glass]
