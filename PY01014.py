'''
CHIA HẾT CHO K
Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
a + b ≤ N
a + b chia hết cho K
Input
Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).
Output
Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.
Nếu không tìm được số nào in ra -1
'''
a,k,n = [int(i) for i in input().split()]
h = a//k
g = n//k
if h*k<a: h += 1 
if h>=g: print(-1)
else:
    for i in range (h,g+1):
        print(i*k-a,end=' ')

