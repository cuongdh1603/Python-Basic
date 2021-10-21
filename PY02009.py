'''
TRÚNG THƯỞNG

Chung kết Euro 2020, quá nhiều người dự đoán đúng Italia thắng Anh bằng đá luân lưu 11m. Ban tổ chức chương trình Dự đoán tỉ số trúng Mercedes thấy rất khó trao giải nên quyết định tìm người được trao thưởng bằng cách chạy đoạn code lựa chọn ngẫu nhiên.
Các người chơi dự đoán đúng được đánh số thứ tự bắt đầu từ 1, giả sử cũng có không quá 1000 người. Chương trình sẽ thực hiện lấy ngẫu nhiên N lần, mỗi lần 1 giá trị từ 1 đến 1000, N cũng không quá 1000.
Sau khi kết thúc N lần ngẫu nhiên, con số nào được chọn nhiều lần nhất sẽ cho biết người trúng thưởng. Trong trường hợp có nhiều số có số lần xuất hiện bằng nhau và lớn nhất thì số có giá trị nhỏ nhất sẽ được chọn.
Hãy giúp BTC tìm ra người được trao thưởng.

Input
Dòng đầu ghi số bộ test, không quá 100.
Mỗi bộ test gồm N+1 dòng. Dòng đầu ghi số N. Tiếp theo là N dòng ghi các giá trị ngẫu nhiên nhận được.

Output
Với mỗi test, ghi ra số thứ tự của người được trao thưởng.
'''
t = int(input())
while t>0:
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    a.sort()
    val = a[0]
    d = 1
    i = 1 
    tmp = 1
    while i < n:
        if a[i] != a[i-1]:
            if tmp > d:
                d = tmp
                val = a[i-1]
            tmp = 1
        elif i==n-1:
            tmp += 1
            if tmp > d:
                val = a[i]
        else: tmp += 1
        i += 1
    print(val)
    t-=1
'''
3
3
999
999
19
4
13
333
333
13
3
11
12
13  
'''