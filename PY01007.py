'''
LÃI SUẤT NGÂN HÀNG

Ngân hàng thông báo lãi suất là X % mỗi năm.
Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.
Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.

Input
Dòng đầu ghi số bộ test.
Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0<N<M<100000.

Output
Ghi ra số năm tính được.
'''
t = int(input())
while t>0:
    n,x,m = [float(i) for i in input().split()]
    dem = 0
    while n<m:
        n += n*x/100
        dem += 1
    print(dem)
    t -= 1
'''
2

200.00 6.5 300

500 4 1000.00
'''