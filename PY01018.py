#MÃ HÓA 2
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
p = list(p)
while True:
    a = list(input().split())
    if len(a)==1: break
    k = int(a[0])
    s = list(a[1])
    for i in range(0,len(s)):
        s[i] = p[(p.index(s[i])+k)%28]
    s.reverse()
    print(''.join(s))
