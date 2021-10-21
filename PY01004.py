'''
NGUYÊN TỐ

Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1. Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

Input
Dòng đầu ghi số bộ test, không quá 10.
Dòng thứ 2 ghi số N (1 < N < 10000)

Output
Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
import math
def prime(n):
    x = int(math.sqrt(float(n)))
    for i in range (2,x+1):
        if n%i == 0: return False
    return n>1
def co_prime(n):
    k = 0
    for i in range (1,n):
        if math.gcd(i,n)== 1:
            k += 1
    return prime(k)
t = int(input())
while t>0:
    n = int(input())
    if co_prime(n): print("YES")
    else: print("NO") 
    t -= 1