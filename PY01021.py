'''
TÍNH TỔNG CÁC CHỮ SỐ

Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển và nối với tổng các chữ số trong S ở cuối cùng. Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.

Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test là một xâu ký tự S.
T, S thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ Length(S)≤105.
Output:
Đưa ra kết quả mỗi test theo từng dòng.
'''
t = int(input())
while t>0:
    s = input()
    l = len(s)
    dem = 0
    s_1 = ""
    for i in s:
        if i.isdigit():
            dem += int(i)
        else: s_1 += i
    s_1 = list(s_1)
    s_1.sort()
    print(''.join(s_1)+str(dem))
    t -= 1
'''
2
AC2BEW3
ACCBA10D2EW30
'''