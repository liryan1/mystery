def solution(x, y):
    ans = 0
    for i in x:
        ans += x
    for j in y:
        ans -= y
    return ans if len(x) > len(y) else -ans