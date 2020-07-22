/*现给定所有种类月饼的库存量、总售价、以及市场的最大需求量，请你计算可以获得的最大收益是多少。

注意：销售时允许取出一部分库存。样例给出的情形是这样的：假如我们有3种月饼，其库存量分别为18、15、10万吨，
总售价分别为75、72、45亿元。如果市场的最大需求量只有20万吨，
那么我们最大收益策略应该是卖出全部15万吨第2种月饼、以及5万吨第3种月饼，获得 72 + 45/2 = 94.5（亿元）*/

#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<algorithm>
using namespace std;

struct mooncake{
    double store;
    double sell;
    double price;
}cake[1010];
bool cmp(mooncake a,mooncake b){
    return a.price > b.price;
}
int main(){
    int n;
    double D;
    scanf("%d%lf",&n,&D);
    for(int i=0;i<n;i++){
        scanf("%lf",&cake[i].store);
    }
    for(int i=0;i<n;i++){
        scanf("%lf",&cake[i].sell);
        cake[i].price = cake[i].sell/cake[i].store;
    }
    sort(cake,cake+n,cmp);
    double ans = 0;
    for(int i=0;i<n;i++){
        if(cake[i].store <= D){
            D -= cake[i].store;
            ans += cake[i].sell;
        }
        else{
            ans += cake[i].price*D;
            break;
        }
    }
    printf("%2f\n",ans);
    return 0;
}
