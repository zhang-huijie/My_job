x = int(input())
st = input().split(":")
te = int(input())
t = int(st[0])
m = int(st[1])
to_min = t*60 + m
if(to_min >= te):
    hr = (to_min - te) // 60
    t = hr
    m = (to_min - te) - hr * 60
else:
    te = te -to_min
    day = te //(24 * 60)
    te = te - day * 24 * 60
    hr = te // 60
    te = te - hr * 60
    day = day % 7
    x = (x - day  - 1 + 7) % 7
    t = 23 - hr
    m = 60 - te
    if m == 60:
        m = 0
        t = t + 1
    if t == 24:
        x = (x + 1) % 7
        t = 0
print(x)
if t < 10:
    t = '0' + str(t)
if m < 10:
    m = '0' +str(m)
print(str(t) + ":" + str(m))
