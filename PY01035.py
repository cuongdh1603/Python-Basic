'''
HỆ CƠ SỐ 8

Cho một số nhị phân, người ta nhận ra quy tắc đơn giản là chỉ cần xét lần lượt các cụm ba chữ số nhị phân tình từ cuối của số đó, sau đó chuyển lần lượt từng cụm sang giá trị thập phân tương ứng thì kết quả nhận được chính là biểu diễn của số đó trong hệ cơ số 8. Nếu cụm cuối cùng bị thiếu thì bổ sung các chữ số 0 cho đủ 3 chữ số.
Ví dụ:
11001100 => 011 | 001 | 100 => 314
Hãy áp dụng tính chất trên để chuyển đổi một số nhị phân (không quá 100 chữ số và luôn bắt đầu bởi chữ số 1) sang hệ cơ số 8.

Input
Chỉ có một số nhị phân, không quá 100 chữ số

Output
Ghi ra kết quả trong hệ cơ số 8
'''
def charToNum(s):
    return int(ord(s)-ord('0'))
def convert(s):
    c_s = ""
    while len(s)%3 != 0:
        s = '0' + s
    i = 0
    l = len(s)
    while i<l:
        tmp = s[i:i+3]
        val = charToNum(tmp[0])*(2**2) + charToNum(tmp[1])*2 + charToNum(tmp[2])
        c_s += str(val)
        i += 3
    return c_s
s = input()
print(convert(s))