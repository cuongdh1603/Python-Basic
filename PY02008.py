'''
KHOẢNG CÁCH NGUYÊN TỐ
Cho hai số nguyên N và X.
Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.
Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32
Input
Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)
Output
Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.
'''
MXN = 10003
prime = [True for i in range(MXN+1)]
def seive():
    prime[0] = prime[1] = False
    i = 2
    while i*i<=MXN:
        if prime[i] == True:
            for j in range(i*i,MXN,i):
                prime[j] = False
        i += 1
seive()
n,x = [int(i) for i in input().split()]
print(x,end=' ')
p = 0
for i in range(0,n):
    for j in range(p,MXN):
        if prime[j] == True:
            print(x+j,end=' ')
            x += j
            p = j+1
            break