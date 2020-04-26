a = list(map(int,input().rstrip().split()))
T,D,X,N = a[0],a[1],a[2],a[3]#T每隔T分钟烤鱼，D单程取鱼的时间，X吃鱼费时间，N要吃的鱼数目
count_time = 0
count_t = 0
sum_i = 0
for n_i in range(N):
    if T>D+X:
        count_time = T+X
        print(count_time)
    else
        if T<=D+X:
            count_t = count_t+T
            print(T+D+X)+(n_i-1)*(T-D)










