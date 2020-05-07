#include <iostream>
#include <string>
#include <utility>
#include <climits>
#include <algorithm>
//用-1(3,2(0,-1)) 这样的字符串表示一棵二叉树，在这颗二叉树中找到一条节点之和最大的路段
using namespace std;
struct TreeNode {
    TreeNode *left;
    TreeNode *right;
    int val;
    TreeNode(int n): left(NULL), right(NULL), val(n) {}
};


TreeNode* consTree(string s) {
	if (s.size() == 0) {
		return NULL;
	}
	auto left_pos = s.find("(");
	if (left_pos == string::npos) {
		int n = stoi(s);
		if (n == 0) {
			return NULL;
		} else {
			return new TreeNode(n);
		}
	} else {
		auto right_pos = s.rfind(")");
		int n = stoi(s.substr(0, left_pos));
		TreeNode* root = new TreeNode(n);
		string subs = s.substr(left_pos+1, right_pos - left_pos - 1);
		int dot_pos = subs.find(",");
		string left_sub = subs.substr(0, dot_pos);
		string right_sub = subs.substr(dot_pos+1);
		root->left = consTree(left_sub);
		root->right = consTree(right_sub);
		return root;
	}
}


pair<int, int> helper(TreeNode* root) {
	if (!root) {
		return {INT_MIN, 0};
	}
	pair<int, int> left = helper(root->left);
	pair<int, int> right = helper(root->right);
	int cur_max = max({root->val, root->val + left.second, root->val + right.second});
	int total_max = max({cur_max, left.first, right.first});
	// cout << root->val << "   " << cur_max <<" " << left.second << " " << " " << right.second <<" "<< endl;  //left.first << " " << right.first <<endl;
	return {total_max, cur_max};
}

void trave(TreeNode* root) {
	if (!root) {
		return;
	}
	cout << root->val << " ";
	trave(root->left);
	trave(root->right);
}

int main() {
    string s;
    getline(cin, s);
    auto root = consTree(s);
	//trave(root);
	// cout << endl;
	auto ret = helper(root);
	cout << ret.first << endl;
	return 0;
}
