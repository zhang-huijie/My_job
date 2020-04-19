n,k = list(map(int,input().rstrip().split()))
if n == 1:
    print(1)
left = 1
right = n
ans = 0

while left < right:
    mid = (left + right) // 2
    kk = k
    s = mid
    while mid // kk:
        s += mid // kk
        kk = kk * k
    if s >= n:
        ans = mid
        break
    else:
        left = mid + 1
print(ans)


