K = int(input())
S = input()
if len(S) > K:
    ans = S[0:K] + '...'
else:
    ans = S

print(ans)
