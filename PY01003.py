'''
LÀM TRÒN SỐ

Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:
Nếu N>10, làm tròn đến số hàng chục gần nhất
Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
Cứ tiếp tục như vậy …
Chú ý: Giá trị 5 sẽ được làm tròn lên.

Input
Dòng đầu ghi số bộ test (không quá 100)
Mỗi bộ test ghi số N trên một dòng (N nguyên dương và không quá 9 chữ số)

Output
Với mỗi test, ghi ra kết quả làm tròn tương ứng trên một dòng.
'''
t = int(input())
'''
7
15
14
5
99
12345678
44444445
1445
'''
def numDg(n):
    ans = 0
    while n != 0:
        n //= 10
        ans += 1
    return ans
while t>0:
    n = int(input())
    k = numDg(n)
    p = pow(10,k-1)
    for i in range(0,k):
        a = n//pow(10,i)
        b = a+1
        a1 = int(pow(10,i))*a
        b1 = int(pow(10,i))*b
        if b1 - n <= n - a1:
            n = b1
        else: n = a1
        if n%p==0: break
    print(int(n))
    t -= 1
