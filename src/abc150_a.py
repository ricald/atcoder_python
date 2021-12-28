def main():
    K, X = map(int, input().split())

    ans = "No"
    if 500 * K >= X:
        ans = "Yes"

    print(ans)

if __name__ == '__main__':
    main()
