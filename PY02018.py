'''
SỐ NHỎ NHẤT CÒN THIẾU

Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.

Input
Dòng đầu ghi số N (1 <= N <= 30000).
Dòng tiếp theo ghi N số của dãy A (1 <= A[i] <= 30000).

Output
Ghi ra số nhỏ nhất còn thiếu nếu có.
(khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).
'''
n = int(input())
a = list(map(int,input().split()))
a.sort()
min_v = a[0]
max_v = a[n-1]
for i in range(min_v,max_v+2):
    if a.count(i)==0:
        print(i)
        break