'''
LIỆT SỐ FIBONACCI

Dãy số Fibonacci được định nghĩa theo công thức như sau:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 với n>2
Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test viết trên một dòng hai số a và b.

Output
Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống.
'''
ar = [0,1]
def fibo():
    for i in range (2,93):
        x = ar[i-1] + ar[i-2]
        ar.append(x)
t = int(input())
while t>0:
    fibo()
    a,b = [int(i) for i in input().split()]
    for i in range(a,b+1):
        print(ar[i],end=' ')
    print()
    t -= 1