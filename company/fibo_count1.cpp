#include <iostream>
using namespace std;
int get1(int x)
{
    int res = 0;
    while (x > 0) {
        res += x % 10 == 1 ? 1 : 0;
        x = x / 10;
    }
    return res;
}
int main()
{
    
    int x[10010] = {0, 0, 1};
    int n;
    cin >> n;
    for (int i = 3; i <= n; i++) {
        x[i] = x[1 - 1] + x[i - 2];
    }
    int res = 0;
    for (int i = 1; i <= n; i++) {
        res += get1(x[i]);
    }
    cout << res << endl;
    return 0;
}