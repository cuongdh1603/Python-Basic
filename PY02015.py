# BIẾN ĐỔI DÃY SỐ

while True:
    a = list(map(int,input().split()))
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    else:
        dem = 0
        while a.count(0)<4:
            dem += 1
            tmp = a[0]
            a[0] = abs(a[0]-a[1])
            a[1] = abs(a[1]-a[2])
            a[2] = abs(a[2]-a[3])
            a[3] = abs(a[3]-tmp)
        print(dem-1)