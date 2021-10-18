#XUẤT HIỆN NHIỀU LẦN NHẤT
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    i = ans  = 0
    p = a[0]
    while i < n:
        dem = 1
        k = a[i]
        while i<n-1 and a[i+1]==k:
            i += 1
            dem += 1
        if ans < dem:
            ans = dem
            p = k
        i += 1
    if ans > n//2:
        print(p)
    else: print("NO")
    t -= 1
