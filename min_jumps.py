'''
You are given an array of integers, where each element represents 
the maximum number of steps that can be jumped going forward from
that element. Write a function to return the minimum number of
jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, 
as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
'''

def min_jumps(steps: list) -> int:
	n = len(steps)
	table = [0]*n

	for i in range(n-2, -1, -1):
		end = min(i + steps[i], n-1)
		table[i] = min(table[i+1: end+1]) + 1 if i < end else float("inf")

	return table[0]

if __name__ == "__main__":
	test = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
	print(min_jumps(test))