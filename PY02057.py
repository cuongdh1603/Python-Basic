'''
SỐ MAY MẮN TRONG MA TRẬN

Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cạch giữa số lớn nhất và số nhỏ nhất của ma trận.
Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.
Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?

Input
Dòng đầu ghi hai số N và M (1 < N, M < 50)
Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

Output
Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND
'''
n,m = [int(i) for i in input().split()]
a = []
for i in range(0,n):
    b = list(map(int,input().split()))
    a.append(b)
minv = min(min(i) for i in a)
maxv = max(max(i) for i in a)
ans = []
midv = 0
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if a[i][j] == maxv-minv:
            midv = a[i][j]
            ans.append([i,j])
if len(ans) > 0:
    print(midv)
    for i in ans:
        print(f"Vi tri [{i[0]}][{i[1]}]")
else: print('NOT FOUND')
'''
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
'''