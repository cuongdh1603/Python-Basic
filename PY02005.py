#CẶP NGHỊCH THẾ
n = int(input())
a = list(map(int,input().split()))
i = j = dem = 0
for i in range (n-1):
    for j in range (i+1,n):
        if(a[i]>a[j]):
            dem += 1
print(dem)

