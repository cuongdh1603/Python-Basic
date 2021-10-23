s = input()
l = len(s)
a = []
b = []
for i in range(0,l-1,2):
    a.append(s[i:i+2])
    if b.count(s[i:i+2]) == 0:
        b.append(s[i:i+2])
b.sort()
k = int(input())
count = 0
for i in b:
    if a.count(i) >= k:
        print(i,a.count(i))
        count += 1
if count == 0: print('NOT FOUND')
'''
124356141111434356149
2
'''