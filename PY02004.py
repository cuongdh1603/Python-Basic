'''
DÃY SỐ NHỊ PHÂN

Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.
Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

Input
Dòng 1 ghi số N là số phần tử của dãy (không quá 100).
Dòng 2 ghi N số nhị phân.

Output
Ghi ra kết quả bài toán.
'''
n = int(input())
a = list(map(int,input().split()))
dem = 0
for i in range(0,n-1):
    if a[i] != a[i+1]:
        dem += 1
print(dem)