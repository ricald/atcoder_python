def main():
    A = list(map(int, input().split()))

    ans = 'YES' if A.count(5) == 2 and A.count(7) == 1 else 'NO'

    print(ans)

if __name__ == '__main__':
    main()
