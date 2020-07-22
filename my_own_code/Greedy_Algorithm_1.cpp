#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
using namespace std;
 
 
const int maxn = 1010;
int n,d;
int index = 0;
double sum = 0;
double s = 0;
double money = 0;
 
struct mooncake{
	double w;
	double c;
}m[maxn];
 
bool cmp(mooncake c1,mooncake c2){
	return c1.c > c2.c;
}
 
 
int main() {
	scanf("%d%d", &n, &d);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &m[i].w);
		s += m[i].w;
	}
	for (int i = 0; i < n; i++) {
		scanf("%lf", &m[i].c);
		m[i].c = m[i].c / m[i].w;
	}
	sort(m, m + n, cmp);
	while (d > 0 && sum < s) {
		if (d <= m[index].w) {
			money += d * m[index].c;
			sum += d;
			d = 0;
		}
		else if (d > m[index].w) {
			money += m[index].c * m[index].w;
			sum += m[index].w;
			d -= m[index].w;
		}
		index++;
	}
	printf("%.2f\n", money);
	return 0;
}