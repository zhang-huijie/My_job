import math
n, m = list(map(int, input().rstrip().split()))
stocks = list(map(int, input().rstrip().split()))
nquery = int(input().rstrip())

ans = []
for _ in range(nquery):
    nsell = int(input().rstrip())
    to_sell = stocks[0:nsell]
    to_sell.reverse()
    cost = 0
    days = math.ceil(nsell / m)
    left = 0
    for day in range(days):
        right = min(left+m, len(to_sell))
        for sell in to_sell[left : right]:
            cost += (day+1) * sell
        left = right
    ans.append(cost)

for a in ans:
    print(a)
        