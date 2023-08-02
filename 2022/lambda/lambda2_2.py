''' Gearing Up for Destruction
    ==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.
'''

from fractions import Fraction

def solution0(pegs):
    '''Not working... some bugs exist'''
    n = len(pegs)
    if n == 2:
        return [(pegs[1] - pegs[0]) * 2, 3]
    # Construct distances list
    distances = [0] * (n - 1)
    for i in range(n-1):
        distances[i] = pegs[i+1] - pegs[i]
    
    # Compute all radii except first and last
    # using recurrence relation r_k = d_k - r_k + 1
    # Setting r_n = 1/2 r_1, compute distances from end
    radii = [0] * n
    radii[n-2] = distances[-1]
    for i in range(n - 3, -1, -1):
        radii[i] = distances[i] - radii[i+1]
    print("first pass radii:", radii)
    # Compute first and last radii from distances
    if n % 2 == 0:
        radii[0] = Fraction(radii[0]*3, 2)
        sign = 1
    else:
        radii[0] = Fraction(radii[0]*2, 1)
        sign = -1
    
    radii[-1] = radii[0] / 2
    if radii[0] <= 0:
        return [-1, -1]
    # Update radii
    for i in range(1, n - 2):
        radii[i] = radii[i] + sign * Fraction(radii[0], 2)
        if radii[i] <= 0:
            return [-1, -1]
        sign *= (-1)
    print(radii)
    return [radii[0].numerator, radii[0].denominator]


def solution(pegs):
    n = len(pegs)
    if n < 2:
        return [-1, -1]

    even = True if n % 2 == 0 else False
    # Solving the system of equations, the equation is:
    # odd
    # r[0] = 2 * (-pegs[0] + 2 *(pegs[1] - pegs[2] + pegs[3] -
    # ... + pegs[n-2]) - pegs[n-1])
    # even
    # r[0] = 2/3 * (-pegs[0] + 2 *(pegs[1] - pegs[2] + pegs[3] -
    # ... - pegs[n-2]) + pegs[n-1])
    if even:
        summation = pegs[n-1] - pegs[0]
    else:
        summation = - pegs[n-1] - pegs[0]

    for i in range(1, n-1):
        summation += 2 * (-1)**(i+1) * pegs[i]

    if even:
        radius0 = Fraction(2*summation, 3).limit_denominator()
    else:
        radius0 = Fraction(2*summation, 1).limit_denominator()
    if radius0 <= 2:
        return [-1, -1]

    # Check whether radii are too small
    current = radius0
    for i in range(0, n-2):
        distance = pegs[i+1] - pegs[i]
        next = distance - current
        if (current < 1 or next < 1):
            return [-1, -1]
        current = next
    return [radius0.numerator, radius0.denominator]


def main():
    pegs_list = [
        [4, 30, 50],
        [4, 17, 50],
        [1, 31],
        [1, 51],
        [1, 31, 51, 71],
        [1, 31, 51, 71, 91],
        [4, 9, 17, 31, 40],
    ]
    for pegs in pegs_list:
        print("INPUT:", pegs)
        print(solution(pegs))

if __name__ == "__main__":
    main()