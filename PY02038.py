'''
ĐẾM CẶP ĐỒNG XU

Cho một lưới hình vuông kích thước N*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.

Input
Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)

Output
Ghi ra số cặp đồng xu đếm được.
'''
factor = [1,1]
def create():
    for i in range(2,100):
        factor.append(factor[len(factor)-1]*i)
def solve(n):
    return factor[n]//(factor[2]*factor[n-2])
n = int(input())
s = []
ans = 0
create()
for i in range(0,n):
    str = input()
    s.append(str)
    ans += solve(str.count("C"))
for i in range(0,n):
    c = 0
    for j in range(0,n):
        if s[j][i] == "C":
            c += 1
    if c > 1: ans += solve(c)
print(ans)
'''
4
CC..
C..C
.CC.
.CC.
'''