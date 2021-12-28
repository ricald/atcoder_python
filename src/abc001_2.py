def main():
    m = int(input())

    if m < 100:
        ans = '{:0=2}'.format(int(0))
    elif m >= 100 and m <= 5000:
        ans = '{:0=2}'.format(int(m / 100))
    elif m >= 6000 and m <= 30000:
        ans = '{:0=2}'.format(int(m / 1000 + 50))
    elif m >= 35000 and m <= 70000:
        ans = '{:0=2}'.format(int((m / 1000 - 30) / 5 + 80))
    elif m > 70000:
        ans = '{:0=2}'.format(int(89))

    print(ans)

if __name__ == '__main__':
    main()
