'''
TỔNG SỐ NGUYÊN LỚN

Cho hai xâu ký tự A và B mô tả hai số nguyên dương lớn có thể có đến 1000 chữ số.
Có thể có các chữ số 0 ở đầu của A và B.
Hãy tính tổng A + B.
Kết quả ghi ra cần loại bỏ các chữ số 0 ở đầu nếu có.

Input
Có hai dòng ghi 2 số A và B.

Output
Ghi ra kết quả A + B.
'''
a = input()
b = input()
ans = ""
rem = 0
while len(a) < len(b): a = '0' + a
while len(b) < len(a): b = '0' + b
for i in range(len(a)-1,-1,-1):
    val = ord(a[i])+ord(b[i])- 2*ord('0')+rem
    if val>9:
        ans = str(val%10) + ans
        rem = 1
    else:
        ans = str(val) + ans
        rem = 0
if rem==1: ans = '1' + ans
while len(ans) > 1 and ans[0] == '0':
    ans = ans[1:]
print(ans)
'''
121212121212121212
45678978
'''