'''
TÂN SUẤT LẺ

Cho dãy số A[] gồm có N phần tử. Các phần tử trong dãy số đều xuất hiện với tần suất chẵn, chỉ có duy nhất 1 số có số lần xuất hiện là số lẻ. Nhiệm vụ của bạn là hãy tìm số này.

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu. N là một số lẻ.
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).

Output: 
Với mỗi test in ra trên mỗi dòng một số nguyên là đáp án của bài toán.
'''
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    st = set(a)
    for i in st:
        if a.count(i)%2==1:
            print(i)
            break
    t -= 1
'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
'''