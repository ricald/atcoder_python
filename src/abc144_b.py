def Calc(N):
    for i in range(1, 9 + 1):
        for j in range(1, 9 + 1):
            if i * j == N:
                return "Yes"
    return "No"

N = int(input())
print(Calc(N))
