#DÃY SỐ PHÙ HỢP
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    i = check = 0
    for i in range(n):
        if(a[i]>b[i]):
            check = 1
            break
    if check: print("NO")
    else: print("YES")
    t -= 1

