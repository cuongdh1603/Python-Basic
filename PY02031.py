#KIỂM TRA NGUYÊN TỐ
import math
def prime(n):
    x = int(math.sqrt(float(n)))
    for i in range (2,x+1):
        if n%i == 0: return False
    return n>1
n,m = [int(i) for i in input().split()]
matrix = []
for i in range (n):
    a = [int(i) for i in input().split()]
    for j in range (m):
        if prime(a[j]): a[j] = 1
        else: a[j] = 0
    matrix.append(a)
for i in range (n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()

