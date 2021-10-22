'''
SẮP XẾP CHẴN LẺ

Cho dãy số A[] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.
In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

Input
Dòng đầu ghi số n (1 < n ≤ 1000)
Các dòng tiếp theo ghi đủ n số của dãy A[], các số đều nguyên dương và không quá 1000.

Output
Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.
'''
n = int(input())
a = []
while len(a) < n:
    b = list(map(int,input().split()))
    a.extend(b)
chan = []
le = []
for i in a:
    if i%2==0: chan.append(i)
    else: le.append(i)
chan.sort()
le.sort(reverse=True)
j = k = 0
for i in range(0,len(a)):
    if a[i]%2==0:
        print(chan[j],end=' ')
        j += 1
    else:
        print(le[k],end=' ')
        k += 1