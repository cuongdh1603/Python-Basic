'''
ĐOẠN CUỐI NGUYÊN TỐ

Cho số nguyên dương N có không quá 500 chữ số.
Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.
Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

Output
Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
'''
def prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def check(n):
    n = n[len(n)-4:]
    if(prime(int(n))): return True
    return False
for t in range(int(input())):
    print('YES' if check(input()) else 'NO')
'''
3
12234323130097
3443354654654654461123
43543543434554659999
'''