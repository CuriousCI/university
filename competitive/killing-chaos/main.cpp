#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

struct SegmentTree {
  using Node = int;
  Node unit = Node(0); // s . t . for every x merge(x , unit ) = x
  Node merge(Node a, Node b) { return a + b; }
  int n;
  vector<Node> st;
  SegmentTree(const vector<int> &data) {
    n = 1;
    while (n < ssize(data))
      n *= 2;
    st.assign(2 * n, unit);
    for (int i = 0; i < ssize(data); i++)
      st[i + n] = Node{data[i]};
    for (int i = n - 1; i > 0; i--)
      st[i] = merge(st[2 * i], st[2 * i + 1]);
  }
  void update(int p, int v) {
    st[p += n] = Node{v};
    for (p /= 2; p > 0; p /= 2)
      st[p] = merge(st[2 * p], st[2 * p + 1]);
  }
  Node query(int x, int y) { // [ x , y ]
    Node left = unit, right = unit;
    for (x += n, y += n + 1; x < y; x /= 2, y /= 2) {
      if (x & 1)
        left = merge(left, st[x++]);
      if (y & 1)
        right = merge(st[--y], right);
    }
    return merge(left, right);
  }

  bool cmp(Node nd, int k) { return nd >= k; }
  int lower_bound(int k) {
    if (!cmp(st[1], k))
      return -1;
    int p = 1;
    Node part = unit;
    while (p < n) {
      p <<= 1;
      if (!cmp(merge(part, st[p]), k)) {
        part = merge(part, st[p++]);
      }
    }
    return p - n;
  }
};

struct RNode {
  int start, end;
  RNode *left, *right;

  RNode(int start, int end) {
    this->start = start;
    this->end = end;
    this->left = NULL;
    this->right = NULL;
  }

  pair<int, int> split(int index) {
    if (this->left) {
      if (this->left->end >= index)
        this->left->split(index);
      else
        this->right->split(index);
    } else {
      this->left = new RNode(this->start, index);
      this->right = new RNode(index, this->end);
    }
  }
};

int round_up(int number) { return number + (10 - (number % 10)); }

int main() {
  int n;
  cin >> n;

  vector<int> train;
  // vector<int> prefix_sum;
  // int total = 0;
  for (int i = 0; i < n; i++) {
    int coach;
    cin >> coach;
    train.push_back(coach);
    // total += coach;
    // prefix_sum.push_back(total);
  }

  set<pair<int, int>> rs;
  rs.insert({0, n});

  for (int i = 0; i < n; i++) {
    int destroyed_coach;
    cin >> destroyed_coach;
  }

  // vector<bool> is_start;
  // vector<bool> is_end;
  //
  // for (int i = 0; i < n; i++) {
  //   is_start.push_back(false);
  //   is_end.push_back(false);
  // }

  // auto seg_tree = SegmentTree(train);
  //
  // int max_chaos = round_up(seg_tree.query(0, train.size()));
  // cout << max_chaos << endl;
  // for (int i = 0; i < destroy_order.size(); i++) {
  // }
}
