#SỐ KHÔNG GIẢM
t = int(input())
while t>0:
    s = input()
    n = len(s)
    i = check = 0
    for i in range(n-1):
        if(int(s[i])>int(s[i+1])):
            check = 1
            break
    if check: print("NO")
    else: print("YES")
    t -= 1
