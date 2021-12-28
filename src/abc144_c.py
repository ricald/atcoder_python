import math
N = int(input())
print(min([a + N // a - 2 for a in range(math.floor(math.sqrt(N)) + 1, 0, -1) if N % a == 0]))
