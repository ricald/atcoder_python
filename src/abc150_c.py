import itertools


def main():
    N = int(input())
    P = tuple(filter(None, input().split()))
    Q = tuple(filter(None, input().split()))

    l = [str(i) for i in range(1, N + 1)]

    permutations = list(itertools.permutations(l, N))
    ans = abs(permutations.index(P) - permutations.index(Q))

    print(ans)

if __name__ == '__main__':
    main()
