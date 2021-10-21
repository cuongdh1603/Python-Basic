'''
SỐ MAY MẮN - 1

Chữ số 4 và chữ số 7được xem là các chữ số may mắn.
Cho số nguyên dương N có không quá 18 chữ số. Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

Input
Chỉ có số N

Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
'''
s = input()
s = list(s)
d4 = s.count('4')
d7 = s.count('7')
if d4+d7==4 or d4+d7==7: print("YES")
else: print("NO")