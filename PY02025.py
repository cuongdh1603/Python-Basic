'''
TẬP HỢP SỐ NGUYÊN

Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].
Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.

Input
Dòng đầu ghi 2 số n và m (1 < n,m <100).
Dòng thứ 2 ghi n số của a[].
Dòng thứ 3 ghi m số của b[].
Các số đều dương và nhỏ hơn 1000.  

Output
Dòng đầu ghi tập giao của A và B
Dòng thứ 2 ghi tập A – B
Dòng thứ 3 ghi tập B - A
'''
n,m = [int(i) for i in input().split()]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sa = set(a)
sb = set(b)
s1 = set(sa & sb)
s2 = set(sa - sb)
s3 = set(sb - sa)
l1 = list(s1)
l2 = list(s2)
l3 = list(s3)
l1.sort()
l2.sort()
l3.sort()
for i in l1:
    print(i,end=' ')
print()
for i in l2:
    print(i,end=' ')
print()
for i in l3:
    print(i,end=' ')
print()
