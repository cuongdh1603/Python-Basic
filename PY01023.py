'''
PHÂN TÍCH THỪA SỐ NGUYÊN TỐ

Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.

Input
Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.

Output
Ghi ra kết quả phân tích theo mẫu như trong ví dụ.
'''
t = int(input())
while t>0:
    a = []
    n = int(input())
    while n%2==0:
        n//=2
        a.append(2)
    u = 3
    while n>=u:
        if n%u == 0:
            while n%u == 0:
                n//=u
                a.append(u)
        else: u += 2
    if n>1: a.append(n)
    st = set(a)
    lt = list(st)
    lt.sort()
    l = len(st)
    print(1,end='')
    for i in lt:
        c = a.count(i)
        print(' * '+str(i)+'^'+str(c),end='')
    print()
    t -= 1