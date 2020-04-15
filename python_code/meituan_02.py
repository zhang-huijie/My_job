import functools

n = int(input())
start = list(map(int,input().rstrip().split()))
end = list(map(int,input().rstrip().split()))
di = {}
for i in range(n):
    di[start[i]] = i
arrive = [di[j] for j in end]
ans = 0
arrive.reverse()
m = arrive[0]
for i in range(1,n):
    if arrive[i] > m:
        ans += 1
    m = min(m,arrive[i])

print(ans)
