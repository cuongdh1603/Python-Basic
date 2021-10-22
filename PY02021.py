'''
DÃY CON CHUNG CỦA BA DÃY SỐ

Cho dãy số A[], B[] và C[] là dãy không giảm và có lần lượt N, M, K phần tử. Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm số nguyên N, M và K (1≤ N, M, K ≤ 100 000).
Dòng tiếp theo gồm N số nguyên A[i], rồi M số nguyên B[i] và K số nguyên C[i].
(0 ≤ A[i], B[i], C[i] ≤ 109).

Output: 
Với mỗi test, in ra trên một dòng là đáp án thu được. Nếu không tìm được đáp án, in ra “NO”.
'''
t = int(input())
while t>0:
    m,n,k = [int(i) for i in input().split()]
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    pa = 0
    pb = 0
    pc = 0
    check = 0
    while pa<m and pb<n and pc < k:
        ans = min(a[pa],b[pb],c[pc])
        if ans == a[pa] and ans == b[pb] and ans == c[pc]:
            print(ans,end=' ')
            check = 1
            pa += 1
            pb += 1
            pc += 1
        else:
            if ans == a[pa]: pa += 1
            if ans == b[pb]: pb += 1
            if ans == c[pc]: pc += 1
    if check == 0: print('NO')
    print()
    t -= 1
    '''
        3
        6 5 8
        1 5 10 20 40 80
        5 7 20 80 100
        3 4 15 20 30 70 80 120
        3 5 4
        1 5 5
        3 4 5 5 10
        5 5 10 20
        3 3 3
        1 2 3
        4 5 6
        7 8 9
        '''