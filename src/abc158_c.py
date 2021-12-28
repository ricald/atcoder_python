import math

A, B = map(int, input().split())

for i in range(1, 1009 + 1):
    if math.floor(i * 0.08) == A and math.floor(i * 0.10) == B:
        answer = i
        break
else:
    answer = -1

print(answer)