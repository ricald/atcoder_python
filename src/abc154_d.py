from collections import deque

N, K = map(int, input().split())
p = list(map(int, input().split()))

queue = deque()
currentSum = 0
maxSum = 0
for i in range(len(p)):
    currentSum = currentSum + p[i] + 1
    queue.append(p[i] + 1)
    if i >= K:
        currentSum = currentSum - queue.popleft()

    if i >= K - 1:
        maxSum = max(maxSum, currentSum)

print("{:.12f}".format(maxSum / 2))
