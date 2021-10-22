'''
HIỆU SỐ NGUYÊN LỚN

Cho hai xâu ký tự A và B mô tả hai số nguyên dương lớn có thể có đến 1000 chữ số.
Có thể có các chữ số 0 ở đầu của A và B.
Hãy tính A - B.
Kết quả có thể âm, khi ghi ra cần loại bỏ các chữ số 0 ở đầu nếu có.
Tất nhiên nếu kết quả là -0 thì ghi ra là 0.

Input
Có hai dòng ghi 2 số A và B.

Output
Ghi ra kết quả A - B.
'''
a = input()
b = input()
ans = ""
rem = 0
while len(a) < len(b): a = '0' + a
while len(b) < len(a): b = '0' + b
less = False
if a != b:
    if a<b:
        less = True
        a,b = b,a
    for i in range(len(a)-1,-1,-1):
        if int(ord(a[i])) >= int(ord(b[i]))+rem:
            val = int(ord(a[i])-ord(b[i]))-rem
            ans = str(val) + ans
            rem = 0
        else:
            val = 10+int(ord(a[i])-ord(b[i]))-rem
            ans = str(val) + ans
            rem = 1
else: ans = '0'
while len(ans)>1 and ans[0] == "0":
    ans = ans[1:]
if less:
    if ans != '0': ans = '-' + ans
print(ans)