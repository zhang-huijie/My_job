stations = list(map(int,input().rstrip().split(',')))
light = list(map(int,input().rstrip().split(',')))
stations.sort()
light.sort()

nstation = len(stations)
nlight = len(light)

min_left = light[0]-stations[0]
min_right = stations[nstation-1]-light[nlight-1]

min_mid = -1
for index in range(nlight-1):
    i = light[index]
    next_i = light[index+1]
    mid = (i+next_i)//2
    l = -1
    for j in range(i+1,mid+1):
        if j in stations and j>i and j <= mid:
            l = max(l,j-i)
    r = -1
    for j in range(mid+1,next_i):
        if j in stations and j>mid and j<next_i:
            r = max(r,next_i-j)
    min_mid = max([l,r,min_mid])
print(max([min_left,min_right,min_mid]))