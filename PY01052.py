'''
TỔNG CHỮ SỐ NGUYÊN TỐ

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
import math
def prime(n):
    x = int(math.sqrt(float(n)))
    for i in range (2,x+1):
        if n%i == 0: return False
    return n>1
def sum(n):
    m = 0
    while n>0:
        m += n%10
        n //= 10
    return m
t = int(input())
while t>0:
    n = int(input())
    if(prime(sum(n))):
        print('YES')
    else: print('NO')
    t -= 1
'''
2

12341

22222222222222222222
'''