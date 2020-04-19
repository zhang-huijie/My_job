#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

void DFS(string cur, vector<bool> used,
  vector<int> &nums, vector<string> &ret, unordered_map<string, int> &map) {
    if (cur.size() == 3 && map.find(cur) == map.end()) {
      ret.push_back(cur);
      map[cur] = 1;
      return;
    }
    if (cur.size() == 3) return;
    for (int i = 0; i < nums.size(); ++i) {
      if (!used[i]) {
        string s = cur + to_string(nums[i]);
        used[i] = true;
        DFS(s, used, nums, ret, map);
        used[i] = false;
      }
    }
}

int main() {
  vector<int> nums = {1,2,3,4};
  vector<bool> used(4, false);
  unordered_map<string, int> map;
  vector<string> ret;
  DFS("", used, nums, ret, map);
  cout << ret.size() << endl;
}