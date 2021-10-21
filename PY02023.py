'''
SẮP XẾP THEO TỔNG CHỮ SỐ

Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

Input
Dòng đầu ghi số bộ test (không quá 10)
Mỗi bộ test gồm 2 dòng:
Dòng đầu là số N (N < 100)
Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.
Output
Với mỗi bộ test, ghi trên một dòng dãy số kết quả.
'''
t = int(input())
def sum(n):
    s = 0
    while n>0:
        s += n%10
        n//=10
    return s
def condition_sort(x):
    s = sum(x)
    val = x
    return (s,x)
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key=condition_sort)
    str_a = [str(int) for int in a]
    print(' '.join(str_a))
    t -= 1
'''
1
8
143 31 22 99 7 9 1111 10000000
'''