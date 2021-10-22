'''
SỐ XEN KẼ

Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:
    Số chữ số là số lẻ
    Chữ số đầu tiên khác chữ số thứ hai.
    Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
Viết chương trình kiểm tra một số có phải xen kẽ hay không.

Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi bộ test viết trên một dòng số cần kiểm tra, không quá 500 chữ số.

Output
Với mỗi bộ test viết ra YES hoặc NO tùy thuộc kết quả kiểm tra
'''
t = int(input())
def c1(n):
    return len(n)%2 == 1
def c2(n):
    if(len(n)>2): return n[0]!=n[1]
    return True
def c3(n):
    for i in range(2,len(n),2):
        if n[i] != n[i-2]:
            return False
    return True
while t>0:
    n = input()
    if c1(n) and c2(n) and c3(n): print('YES')
    else: print('NO')
    t -= 1