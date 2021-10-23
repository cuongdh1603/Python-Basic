n = int(input())
a = list(map(int,input().split()))
b = []
def prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0: return False
    return True
min_pos = -1
for i in a:
    if b.count(i) == 0:
        b.append(i)
for i in range(0,len(b)):
    if prime(sum(b[:i+1])) and prime(sum(b[i+1:])):
        min_pos = i
        break
print(min_pos if min_pos > -1 else 'NOT FOUND')
'''
10
3 6 7 3 5 7 3 6 6 7
'''