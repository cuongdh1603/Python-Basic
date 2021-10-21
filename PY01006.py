'''
SỐ MAY MẮN - 2

Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7. Cho số nguyên dương N không quá 200 chữ số. Hãy kiểm tra xem N có phải số may mắn hay không.

Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi test ghi số nguyên dương N không quá 200 chữ số.

Output
Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
'''
t = int(input())
while t>0:
    s = input()
    d4 = s.count('4')
    d7 = s.count('7')
    if d4 + d7 == len(s):
        print('YES')
    else: print('NO')
    t -= 1
'''
3

4477

44444487777777777

47474747474777777777777744444
'''