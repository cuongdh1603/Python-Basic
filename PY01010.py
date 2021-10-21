'''
ĐẦU CUỐI
Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó thì sẽ tạo ra số có hai chữ số giống nhau hay không?
Input
Dòng đầu ghi số số test (không quá 20). Mỗi test là 1 số nguyên dương N có ít nhất 4 chữ số, nhưng không quá 18 chữ số.
Output
Ghi ra YES hoặc NO
'''
'''
3
12321
1234512
10233211111
'''
t = int(input())
while t>0:
    s = input()
    l = len(s)
    s1 = s[:2]
    s2 = s[l-2:]
    if s1 == s2:
        print('YES')
    else:
        print('NO')
    t -= 1