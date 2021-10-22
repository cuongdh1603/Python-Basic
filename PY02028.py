'''
SẮP XẾP NGUYÊN TỐ

Cho dãy số nguyên dương A[] có N phần tử. Các giá trị trong dãy không quá 1000.
Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.
Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.

Input
Dòng đầu ghi số N (1 < N < 100), dòng thứ 2 ghi N số của dãy A[].

Output
Ghi ra dãy số kết quả trên một dòng.
'''
import math
def prime(n):
    if n < 2: return False
    for i in range (2,int(n**0.5)+1):
        if n%i == 0: return False
    return True
n = int(input())
a = list(map(int,input().split()))
prime_a = []
for i in a:
    if prime(i):
        prime_a.append(i)
prime_a.sort()
j = 0
for i in a:
    if prime(i):
        print(prime_a[j],end=' ')
        j += 1
    else:
        print(i,end=' ')
'''
8
4 6 3 8 7 2 5 9
'''