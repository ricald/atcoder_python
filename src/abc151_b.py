N, K, M = map(int, input().split())

A = list(map(int, input().split()))

need = M * N - sum(A)
if need > K:
    ans = -1
elif need >= 0:
    ans = need
else:
    ans = 0

print(ans)