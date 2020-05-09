
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    vector<int> nums;
    int x = 0;
    while (cin >> x) {
        nums.push_back(x);
    }
    unordered_map<int, bool> count;
    for (int n : nums) {
        count[n] = false;
    }
    cout << nums[0] << " " << nums[0] << " " << nums[0];
    count[nums[0]] = true;
    for (int n : nums) {
        if (!count[n]) {
            cout << " " <<n << " " << n << " " << n;
            count[n] = true;
        }
    }
    cout << '\n';
    return 0;
}
///给一个有序链表，把其中所有的数字的出现次数变为3次，大于3次的删除，少于3次的增加