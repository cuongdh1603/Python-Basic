'''
LIỆT KÊ CÁC SỐ CÓ HAI CHỮ SỐ THEO THỨ TỰ XUẤT HIỆN

Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.
Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.
Hãy liệt kê các số khác nhau xuất hiện trong A[] theo thứ tự xuất hiện.

Input
Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

Output
Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A[] theo thứ tự xuất hiện, mỗi số viết cách nhau một khoảng trống.
'''
s = input()
l = len(s)
rs = []
for i in range(0,l-2,2):
    if rs.count(s[i:i+2])==0:
        rs.append(s[i:i+2])
for i in rs:
    print(i,end=' ')
'''
124356141111434356149
'''
