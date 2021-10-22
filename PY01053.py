'''
SỐ CHIA HẾT CHO 3

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem N có chia hết cho 3 hay không.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
t = int(input())
while t>0:
    n = int(input())
    if n%3 == 0: print('YES')
    else: print('NO')
    t -= 1