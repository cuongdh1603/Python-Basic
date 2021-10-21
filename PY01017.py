#MÃ HÓA 1
t = int(input())

while t>0:
    s = input()
    st = ''
    l = len(s)
    i = 0
    while i<l:
        dem = 1
        k = s[i]
        while i<l-1 and s[i+1] == k:  
            i += 1
            dem += 1
        st += str(dem) + k
        i += 1
    print(st)
    t -= 1