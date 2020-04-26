//阿里的笔试第一题4.22号
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool valid(vector<int>& res) {
	int left_max = res[0];
	int right_max = res.back();
	vector<bool> cond(res.size(), false);
	for (int i = 1; i < res.size(); ++i) {
		if (left_max > res[i]) {
			cond[i] = true;
		}
		left_max = max(left_max, res[i]);
	}
	for (int i = res.size()-2; i >= 0; --i) {
		if (right_max > res[i] && cond[i]) {
			return false;
		}
	}
	return true;
}
void DFS(vector<int>& res, int n, int m, long long& ans) {
	if (res.size() > m) {
		return;
	}
	if (res.size() == m && n == 0) {
		if (valid(res)) {
			ans += 1;
		}
	}
	for (int i = 1; i <= n; ++i) {
		res.push_back(i);
		DFS(res, n-i, m, ans);
		res.pop_back();
	}
}
int main() {
	int n, m;
	cin >> n >> m;
	vector<int> res;
	long long ans = 0;
	DFS(res, n, m, ans);
	cout << (ans % ((int)1e9 + 7)) << endl;
}

