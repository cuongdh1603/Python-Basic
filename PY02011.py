'''
BIẾN ĐỔI VỀ DÃY BẰNG NHAU

Cho dãy số A[] có N phần tử là các số nguyên dương.
Mỗi bước bạn được phép thay đổi 1 giá trị trong dãy bằng cách tăng lên 1 hoặc giảm đi 1.
Hãy tính xem cần ít nhất bao nhiêu bước để biến đổi dãy về giá trị bằng nhau, với điều kiện giá trị của dãy bằng nhau đó phải là một trong các giá trị ban đầu của dãy.

Input
Dòng đầu ghi số N là số phần tử của dãy (không quá 200).
Dòng thứ 2 ghi N phần tử của dãy, các phần tử đều nguyên dương và không quá 10000.

Output
Ghi ra tổng số bước ít nhất tìm được và giá trị bằng nhau được chọn.
Trong trường hợp có nhiều giá trị có thể chọn thì chọn số đầu tiên theo thứ tự xuất hiện trong dãy ban đầu.
'''
n = int(input())
a = list(map(int,input().split()))
ope = 0
val = 0
for i in range(0,n):
    dif = 0
    for j in range(0,n):
        dif += abs(a[i]-a[j])
    if i == 0 or dif < ope:
        val = i
        ope = dif
print(f"{ope} {a[val]}")
