'''
NGUYÊN TỐ CÙNG NHAU
Cho dãy số A[] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.
Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.
Input
Dòng đầu ghi số n (không quá 100).
Dòng thứ 2 ghi n số của dãy A[]
Output
Ghi lần lượt các cặp số nguyên tố cùng nhau theo thứ tự tăng dần.
'''
import math
n = int(input())
a = list(map(int,input().split()))
a.sort()
l = len(a)
for i in range(0,l-1):
    for j in range(i+1,l):
        if math.gcd(a[i],a[j]) == 1:
            print(str(a[i])+" "+str(a[j]))
'''
5
3 7 9 6 13
'''