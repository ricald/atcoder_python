def main():
    S = input()
    ans = ''
    for c in S:
        if all([chk not in c for chk in ['a', 'i', 'u', 'e', 'o']]):
            ans += c
    print(ans)

if __name__ == '__main__':
    main()
