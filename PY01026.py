'''
 SẮP ĐẶT LẠI XÂU KÝ TỰ

Cho hai xâu ký tự s1 và s2. Xâu s2 được gọi là một “sắp đặt lại” của xâu s1 nếu tập ký tự của xâu s2 hoàn toàn giống với xâu ký tự s1, tính cả số lần xuất hiện của từng ký tự.
Ví dụ: s2 = “intestg” là sắp đặt lại của xâu “testing”
Còn xâu “aabbbcccc” không được coi là sắp đặt lại của xâu “abc”.
Nhập 2 xâu s1 và s2 có độ dài không quá 1000 ký tự, chỉ bao gồm các ký tự viết thường, không có khoảng trống. Hãy kiểm tra xem s2 có phải là sắp đặt lại của s1 hay không.

Input
Dòng đầu ghi số bộ test, không quá 5000.
Mỗi test ghi trên 2 dòng lần lượt là xâu s1 và s2.

Output
Ghi ra thứ tự bộ test, sau đó là YES hoặc NO tùy thuộc kết quả kiểm tra.
Xem ví dụ để hiểu rõ hơn.
'''
t = int(input())
dem = 1
while t>0:
    s1 = input()
    s2 = input()
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    print('Test '+str(dem)+': ',end='')
    if s1 == s2: print('YES')
    else: print('NO')
    dem += 1
    t -= 1
    '''
    4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
    '''