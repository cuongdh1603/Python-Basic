class Rectangle:
    def __init__(self,w,h,c):
        self.w = w
        self.h = h
        self.c = c.title()
    def valid(self):
        if self.w > 0 and self.h > 0:
            return True
        return False
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.valid():
    print((r.w+r.h)*2, r.w*r.h, r.c)
else: print('INVALID')