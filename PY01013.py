'''
ƯỚC SỐ CHUNG NGUYÊN TỐ

Cho hai số nguyên dương a và b. Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.
Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.

Input
Dòng đầu ghi số bộ test. Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)

Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
'''
import math
def prime(n):
    x = int(math.sqrt(float(n)))
    for i in range (2,x+1):
        if n%i == 0: return False
    return n>1
def sum(n):
    s = 0
    while n>0:
        s += n%10
        n//=10
    return s
t = int(input())
while t>0:
    a,b = [int(i) for i in input().split()]
    x = math.gcd(a,b)
    if prime(sum(x)): print('YES')
    else: print('NO')
    #print(x)
    t -= 1
'''
3
28 42
123 18
550 55
'''