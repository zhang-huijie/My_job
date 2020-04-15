#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <utility>

using namespace std;

bool cmp(pair<string, int> a, pair<string, int> b) {
	return a.second == b.second ? a.first > b.first : a.second > b.second;
}

int main() {
	string s;
	unordered_map<string, int> map;
	getline(cin, s);
	int p1 = 0, p2 = 0;
	while (p1 < s.size()) {
		p2 = p1;
		while (p2 < s.size() && s[p2] != ',') p2++;	
		string name = s.substr(p1, p2-p1);
		auto it = map.find(name);
		if (it != map.end()) {
			map[name] += 1;
		} else {
			map[name] = 1;
		}
		p1 = p2 + 1;
	}

	vector<pair<string, int>> tmp;
	for (auto p : map) {
		tmp.push_back(p);
	}

	sort(tmp.begin(), tmp.end(), cmp);
	cout << tmp[0].first << '\n';

	return 0;
}
