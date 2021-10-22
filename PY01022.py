'''
TỔNG CHỮ SỐ

Cho một số nguyên (có thể âm) không quá 100.000 chữ số. Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó. Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.

Input
Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)

Output
Ghi ra số bước cần thực hiện.
'''
n = input()
def sum(n):
    s = 0
    for i in n:
        s += ord(i) - ord('0')
    return s
dem = 1
while int(sum(n)) > 9:
    n = sum(n)
    n = str(n)
    dem += 1
print(dem)