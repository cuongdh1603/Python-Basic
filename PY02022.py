'''
LIỆT KÊ SỐ NGUYÊN TỐ TRONG DÃY
Cho dãy số nguyên dương A[] có N phần tử. Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.
Các số được liệt kê theo thứ tự xuất hiện.
Input
Dòng đầu ghi số N (không quá 500).
Dòng sau ghi N số của dãy (không quá 6 chữ số).
Output
Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.
'''
import math
def prime(n):
    x = int(math.sqrt(float(n)))
    for i in range (2,x+1):
        if n%i == 0: return False
    return n>1
n = int(input())
a = list(map(int,input().split()))
s = set({})
for i in a:
    if i not in s and prime(i):
        print(f"{i} {a.count(i)}")
        s.add(i)