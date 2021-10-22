'''
CHÈN XÂU

Cho xâu S1 và xâu S2, độ dài không quá 100.
Hãy chèn xâu S2 vào vị trí p trong xâu S1 (vị trí ký tự đầu tiên là vị trí 1).

Input:
Dòng thứ nhất ghi xâu S1
Dòng thứ hai ghi xâu S2
Dòng thứ ba ghi số p (giá trị p đảm bảo nằm trong phạm vi xâu S1)

Output:
Ghi ra kết quả.
'''
str_1 = input()
str_2 = input()
str_1 = list(str_1)
p = int(input())
str_1.insert(p-1,str_2)
print(''.join(str_1))