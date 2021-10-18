#GIẢI MÃ
t = int(input())
while t > 0:
    s = input()
    l = len(s)
    str = ""
    i = j = 0
    for i in range(0,l,2):
        k = int(s[i+1])
        for j in range(k):
            str += s[i]
    print(str)
    t -= 1

