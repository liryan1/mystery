''' Leetcode "Maximize Distance to Closest Person"
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
'''
class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        '''
        idea: do 2 passes
        1. tabulate all distances left of the person
        2. tabulate all distances right of the person
        Then take maximum of min(left, right)
        O(N) time & O(N) space
        '''
        n = len(seats)
        min_dist_right = [-1]*n
        # distance from right
        for i in range(n-1, -1, -1):
            if seats[i] == 0:
                if i == n - 1:
                    min_dist_right[i] = float("inf")
                elif min_dist_right[i+1] == -1: # seat filled
                    min_dist_right[i] = 1
                else:
                    min_dist_right[i] = min_dist_right[i+1] + 1
        
        # distance from left
        min_dist_left = [-1]*n
        for i in range(n):
            if seats[i] == 0:
                if i == 0:
                    min_dist_left[i] = float("inf")
                elif min_dist_left[i-1] == -1:
                    min_dist_left[i] = 1
                else:
                    min_dist_left[i] = min_dist_left[i-1] + 1
                    
        ans = 0
        for i in range(n):
            if seats[i] == 0:
                ans = max(ans, min(min_dist_left[i], min_dist_right[i]))
        return ans