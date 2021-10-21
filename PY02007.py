'''
CHIA DƯ CHO 42

Cho dãy số A có 10 phần tử là các số nguyên dương. Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả các phần tử đều được chia dư cho 42.

Input
Gồm 10 số nguyên dương, viết trên một hoặc nhiều dòng.

Output
Ghi ra các số khác nhau tìm được sau khi đã chia dư cho 42.
'''
a = []
while len(a)<10:
    b = list(map(int,input().split()))
    a.extend(b)
dem = 0
st = set({})
for i in a:
    st.add(i%42)
print(len(st))