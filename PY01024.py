'''
CHẴN - LẺ

Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?
Tổng chữ số của N chia hết cho 10
Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
'''
t = int(input())
def sum(k):
    s = 0
    n = int(k)
    while n>0:
        s += n%10
        n//=10
    return s%10==0
def space(n):
    for i in range(0,len(n)-1):
        if abs(ord(s[i])-ord(s[i+1])) != 2:
            return False
    return True
while t>0:
    s = input()
    l = len(s)
    if sum(s) and space(s):
        print('YES')
    else: print('NO')
    t -= 1
'''
3

1353

246864

123435
'''