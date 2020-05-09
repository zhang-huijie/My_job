#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
//类似背包问题，没想出来最优解，贪心了一下过了80%
int main() {
	int M, N;
	cin >> M >> N;
	vector<int> servers;
	vector<vector<int>> jobs; // 0 mem, 1 cost;
	for (int i = 0; i < M; ++i) {
		int x;
		cin >> x;
		servers.push_back(x);
	}
	for (int i = 0; i < N; ++i) {
		int x, y;
		cin >> x >> y;
		jobs.push_back({x, y});
	}
	sort(servers.begin(), servers.end());
	auto cmp = [](vector<int>& a, vector<int>& b) {
		return a[1] > b[1];
	};
	sort(jobs.begin(), jobs.end(), cmp);
	int ans = 0;
	for (int i = 0; i < jobs.size(); ++i) {
		auto it = lower_bound(servers.begin(), servers.end(), jobs[i][0]);
		if (*it >= jobs[i][0]) {
			int index = it - servers.begin();
			servers[index] -= jobs[i][0];
			ans += jobs[i][1];
			sort(servers.begin(), servers.end());
		}
	}
	cout << ans << endl;
	return 0;
}
