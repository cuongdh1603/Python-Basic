'''
ĐẾM SỐ TRONG XÂU

Cho một ký tự S[] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S[].
Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.
Ví dụ: S[] = “1212121112211221121”, N = 121 thì đáp án là 3. 

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi test gồm hai dòng, dòng đầu là xâu ký tự S[], dòng sau là số N.

Output
Với mỗi bộ test, ghi ra kết quả tính được trên một dòng.
'''
t = int(input())
while t>0:
    p_str = input()
    s_str = input()
    print(p_str.count(s_str))
    t -= 1
'''
2
1212121112211221121
121
2222222222322292
2222
'''