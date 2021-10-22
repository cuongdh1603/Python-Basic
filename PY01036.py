'''
TÍNH TỔNG PHÂN THỨC

Nhập số nguyên dương N (1 < N < 10000).
Viết chương trình tính tổng:
S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
Kết quả được in ra với 6 chữ số phần thập phân.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi test ghi một số N

Output
Với mỗi bộ test, ghi ra kết quả trên một dòng.
'''
t = int(input())
while t>0:
    n = int(input())
    sum = start = 0
    if n%2 == 0: start = 2
    else: start = 1
    for i in range(start,n+1,2):
        sum += 1/i
    print("{:.6f}".format(sum))
    t -= 1