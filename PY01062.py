'''
ƯU THẾ NGUYÊN TỐ

Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
def prime(n):
    if(n<2): return False
    for i in range (2,int(n**0.5)):
        if n%i == 0: return False
    return True
t = int(input())
st = {2,3,5,7}
while t>0:
    s = input()
    l = len(s)
    count = 0
    for i in s:
        if int(i) in st:
            count += 1
    if prime(l) and count > l-count:
        print('YES')
    else: print('NO')
    t-=1
'''
3
1234567
22334455667
23400300489898989
'''