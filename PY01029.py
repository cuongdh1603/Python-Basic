'''
SỐ ĐẢO NGUYÊN TỐ CÙNG NHAU

Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của a và b bằng 1.
Cho số nguyên dương N không quá 9 chữ số. Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi trên một dòng số nguyên dương N, không quá 9 chữ số.

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
import math
def reverse(n):
    tmp = 0
    while n > 0:
        tmp = tmp * 10 + n%10
        n //= 10
    return tmp
t = int(input())
while t>0:
    n = int(input())
    if math.gcd(n,reverse(n)) == 1:
        print('YES')
    else: print('NO')
    t-=1
'''
3
1234567
22334455667
23400300489898989
'''