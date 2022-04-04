'''
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created; Every Facula bomb spontaneously creates a Mach bomb.

Every step we make one choice from the options below:
1. F += M
2. M += F
Start: 1M 1F.

solution(M, F)
Return minimum number of steps to generate M Mach and F Facula bombs or "impossible".
'''
def solution(x, y):
    F, M = int(x), int(y)
    ops = 0
    if F > 2*M:
        n = F // M
        F -= (M * n)
        ops += n
    elif M > 2*F:
        n = M // F
        M -= (F * n)
        ops += n
    while True:
        if F == M and F != 1:
            return "impossible"
        elif F > M:
            F -= M
            ops += 1
        else:
            M -= F
            ops += 1
        if (F == 1 and M == 1) or (F < 1 or M < 1):
            break
        # print('F,', 'M:', F, M)
    return str(ops) if (F == 1 and M == 1) else "impossible"

if __name__ == "__main__":
    F, M = "70", "31"
    print("initial F, M:", F, M)
    print(solution(F, M))