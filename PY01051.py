'''
TỔNG CHỮ SỐ THUẬN NGHỊCH

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.
Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
def sum(n):
    m = 0
    while n>0:
        m += n%10
        n //= 10
    return m
def sym(n):
    m = 0
    tmp = n
    while n>0:
        m = m*10 + n%10
        n //= 10
    return m == tmp and tmp >9
t = int(input())
while t>0:
    n = int(input())
    if(sym(sum(n))):
        print('YES')
    else: print('NO')
    t -= 1
'''
2

12341

22222222222222222222
'''