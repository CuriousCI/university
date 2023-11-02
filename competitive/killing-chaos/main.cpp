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

// 0-5
// 0-1 2-5
// 0-1 2-3 4-5
// 0-1 2-3 4-5
// previous -= current sum in that range += sums in two new ranges!
// return previous * new trains
// Cases:
// 5-5 (destroyed)
// 3-3 (left destroyed) + 4-5 (stayed right)
// 3-4 (left stayed) + 5-5 (right destroyed)

struct RNode {
  int start, end;
  RNode *left, *right;

  RNode(int start, int end) {
    this->start = start;
    this->end = end;
    this->left = NULL;
    this->right = NULL;
  }

  pair<pair<int, int>, pair<int, int>> split(int index) {
    if (this->left) {
      if (this->left->end >= index)
        return this->left->split(index);
      else
        return this->right->split(index);
    } else {
      this->left = new RNode(this->start, index);
      this->right = new RNode(index + 1, this->end);
      // cout << "(" << this->start << ";" << index << ")  (" << index + 1 <<
      // ";"
      //      << this->end << ")" << endl;
      return {{this->start, index}, {index + 1, this->end}};
    }
  }
};

int round_up(int number) { return number + (10 - (number % 10)); }

int main() {
  int n;
  cin >> n;

  vector<int> train;
  for (int i = 0; i < n; i++) {
    int coach;
    cin >> coach;
    train.push_back(coach);
  }

  auto seg_tree = SegmentTree(train);
  auto ranges = RNode(0, n);

  int segments = 1;
  int max_chaos = round_up(seg_tree.query(0, n - 1)) * segments;
  int chaos = max_chaos;

  for (int i = 0; i < n; i++) {
    int destroyed_coach;
    cin >> destroyed_coach;
    destroyed_coach--;

    auto new_ranges = ranges.split(destroyed_coach);
    auto left_range = new_ranges.first;
    auto right_range = new_ranges.second;

    if (left_range.first == left_range.second &&
        right_range.first == right_range.second) {
      chaos -= round_up(train[destroyed_coach]);
      max_chaos = max(max_chaos, chaos * segments);
      segments--;
    } else if (left_range.first == left_range.second) {
      chaos -= round_up(train[destroyed_coach]);
      max_chaos = max(max_chaos, chaos * segments);
    } else if (right_range.first == right_range.second) {
      chaos -= round_up(train[destroyed_coach]);
      max_chaos = max(max_chaos, chaos * segments);
    } else {
      chaos -= round_up(seg_tree.query(left_range.first, right_range.second));
      chaos += round_up(seg_tree.query(left_range.first, left_range.second));
      chaos += round_up(seg_tree.query(right_range.first, right_range.second));
      max_chaos = max(max_chaos, chaos * segments);
      segments++;
    }

    // cout << chaos << " * " << segments << endl;
  }

  cout << max_chaos << endl;
}
