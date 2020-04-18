
def min_lose(a_i,q_all,n,m):
    min_out = []
    a_i = sorted(a_i,reverse=True)
    for i in range(len(q_all)):
        feg = 0
        count = 0
        beishu = 0
        out_q = a_i[n-q_all[i]:]
        for i in range(len(out_q)):
            beishu = feg // m
            count += out_q[i]*(beishu+1)
            feg += 1
        min_out.append(count)
    return min_out
if __name__ == '__main__':

    a = list(map(int,input().rstrip().split()))
    n,m = a[0],a[1]
    a_i = list(map(int,input().rstrip().split()))
    Q = int(input())
    q_all = []
    for i in range(Q):
        q_all.append(int(input()))

    a = min_lose(a_i, q_all, n, m)
    for  i in range(len(a)):
        print(a[i])






