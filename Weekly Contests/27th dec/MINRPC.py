for _ in range(int(input())):
    num = int(input())
    s = input().strip()
    ans = ['P'] * num
    w = num // 2 + 1
    for i in range(num):
        if s[i] == 'R':
            w -= 1
    for i in range(num - 1, -1, -1):
        if w > 0 and (s[i] == 'P' or s[i] == 'S'):
            if s[i]=='P':
                ans[i]='S'
            else:
                ans[i]='R'
            w -= 1

    print("".join(ans))