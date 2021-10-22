'''
CHẴN – LẺ - NGUYÊN TỐ

Cho một số nguyên dương không quá 500 chữ số.
Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?
Vị trí chẵn là chữ số chẵn
Vị trí lẻ là chữ số lẻ
Tổng chữ số là một số nguyên tố.
Input
Dòng đầu ghi số bộ test (không quá 10)
Mỗi bộ test ghi trên một dòng giá trị số nguyên (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
t = int(input())
def prime(n):
    sum = 0
    for i in n:
        sum += ord(i)-ord('0')
    if sum<2: return False
    for i in range(2,int(sum**0.5+1)):
        if sum%i==0: return False
    return True
def pos(n):
    for i in range(0,len(n)):
        if (i%2==0 and (ord(n[i])-ord('0'))%2!=0) or (i%2!=0 and (ord(n[i])-ord('0'))%2==0):
            return False
    return True
while t>0:
    n = input()
    if prime(n) and pos(n): print('YES')
    else: print('NO')
    t -= 1