import math

A, B, H, M = map(int, input().split())
angleH = 360 * ((H + (M / 60)) / 12)
angleM = 360 * (M / 60)
angle = abs(angleH - angleM)
answer = math.sqrt(math.pow(A, 2) + math.pow(B, 2) - (2 * A * B * math.cos(math.radians(angle))))
print(answer)