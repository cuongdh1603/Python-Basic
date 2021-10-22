'''
NGUYÊN TỐ CÙNG NHAU

Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.
Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.
Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.

Input
Chỉ có một dòng ghi hai số N và K

Output
Ghi ra lần lượt các số thỏa mãn theo thứ tự từ nhỏ đến lớn. Mỗi dòng ghi 10 số.
'''
import math
n,k = [int(i) for i in input().split()]
j = 1
for i in range(10**(k-1),10**k):
    if math.gcd(i,n)==1:
        print(str(i)+" ",end=' ')
        if j%10 == 0:
            print()
        j += 1
'''
5

3 7 9 6 13
'''