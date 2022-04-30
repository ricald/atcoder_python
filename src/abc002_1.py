def main():
    X, Y = [int(i) for i in input().split()]
    ans = X if X > Y else Y
    print(ans)

if __name__ == '__main__':
    main()
