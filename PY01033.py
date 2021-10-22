'''
BỘ BA NGUYÊN TỐ CÙNG NHAU

Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.
Cho hai số nguyên dương L và R (10 < L < R < 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].

Input
Chỉ có 2 số L và R

Output
Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.
Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.
'''
import math
l,r = [int(i) for i in input().split()]
for i in range(l,r-1):
    for j in range(i+1,r):
        for k in range(j+1,r+1):
            if math.gcd(i,j) == math.gcd(i,k) == math.gcd(j,k) == 1:
                print(f"({i}, {j}, {k})")