s = input()
c1 = c2 = 0
for i in s:
    if i.isupper():
        c1 += 1
    else:
        c2 += 1
if c1 <= c2:
    print(s.lower())
else:
    print(s.upper())