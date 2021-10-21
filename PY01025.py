'''
CHÈN DẤU PHẨY

Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.
Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.

Input
Chỉ có 1 số N

Output
Kết quả sau khi đã chèn dầu phẩy
'''
from typing import List


s = input()
s = list(s)
l = len(s)
i = 3
while i < l:
    s.insert(l-i,',')
    i += 3
print(''.join(s))