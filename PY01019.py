# XÂU “THĂNG BẰNG”
t = int(input())
while t>0:
    s = input()
    l = len(s)
    s1 = s[l-1::-1]
    check = 1
    for i in range(1,l):
        if abs(int(ord(s[i])-ord(s[i-1]))) != abs(int(ord(s1[i])-ord(s1[i-1]))):
            check = 0
            break
    if check == 0:
        print('NO')
    else: print('YES')
    t -= 1
