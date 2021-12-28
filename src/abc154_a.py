S, T = input().split()
A, B = map(int, input().split())
U = input()
if U == S:
    A = A - 1
else:
    B = B - 1

print("{0} {1}".format(A, B))
