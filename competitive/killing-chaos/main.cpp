#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using ll = long long;
using namespace std;

struct SegmentTree {
  using Node = ll;
  Node unit = Node(0); // s . t . for every x merge(x , unit ) = x
  Node merge(Node a, Node b) { return a + b; }
  ll n;
  vector<Node> st;
  SegmentTree(const vector<ll> &data) {
    n = 1;
    while (n < data.size())
      n *= 2;
    st.assign(2 * n, unit);
    for (ll i = 0; i < data.size(); i++)
      st[i + n] = Node{data[i]};
    for (ll i = n - 1; i > 0; i--)
      st[i] = merge(st[2 * i], st[2 * i + 1]);
  }
  void update(ll p, ll v) {
    st[p += n] = Node{v};
    for (p /= 2; p > 0; p /= 2)
      st[p] = merge(st[2 * p], st[2 * p + 1]);
  }
  Node query(ll x, ll y) { // [ x , y ]
    Node left = unit, right = unit;
    y--;
    for (x += n, y += n + 1; x < y; x /= 2, y /= 2) {
      if (x & 1)
        left = merge(left, st[x++]);
      if (y & 1)
        right = merge(st[--y], right);
    }
    return merge(left, right);
  }

  bool cmp(Node nd, ll k) { return nd >= k; }
  ll lower_bound(ll k) {
    if (!cmp(st[1], k))
      return -1;
    ll p = 1;
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
  ll start, end;
  RNode *left, *right;

  RNode(ll start, ll end) {
    this->start = start;
    this->end = end;
    this->left = NULL;
    this->right = NULL;
  }

  pair<pair<ll, ll>, pair<ll, ll>> split(ll index) {
    if (this->left) {
      if (this->left->end >= index)
        return this->left->split(index);
      else
        return this->right->split(index);
    } else {
      if (this->start == index) {
        ll old_start = this->start;
        this->start = index + 1;
        return {{old_start, index}, {index + 1, this->end}};
      } else if (this->end == index) {
        ll old_end = this->end;
        this->end = index - 1;
        return {{this->start, index}, {index + 1, old_end}};
      } else {
        this->left = new RNode(this->start, index);
        this->right = new RNode(index + 1, this->end);
        return {{this->start, index}, {index + 1, this->end}};
      }
    }
  }
};

ll round_up(ll number) {
  return number % 10 ? number + (10 - (number % 10)) : number;
}

int main() {
  cin.tie(0)->sync_with_stdio(false);
  ll n;
  cin >> n;

  vector<ll> train;
  for (ll i = 0; i < n; i++) {
    ll coach;
    cin >> coach;
    train.push_back(coach);
  }

  auto seg_tree = SegmentTree(train);
  // auto ranges = RNode(0, n);

  ll segments = 1;
  ll sum = seg_tree.query(0, n);
  ll max_chaos = round_up(sum) * segments;
  ll chaos = max_chaos;

  map<pair<ll, ll>, ll> calculated;
  set<pair<ll, ll>> rang;
  rang.insert({0, n});
  // rang.push_back();
  // upper_bound (rang.begin(), rang.end(), {});
  // for (int i = 0;
  // priority_queue<pair<ll, ll>> rang;
  // rang.push({0, n});
  // rang.pop({3, 3});
  // set<pair<ll, ll>> rang;
  // rang.insert({0, n});
  calculated[{0, n}] = sum;

  for (ll i = 0; i < n / 2; i++) {
    ll destroyed_coach;
    cin >> destroyed_coach;
    destroyed_coach--;

    // if (this->start == index) {
    //   ll old_start = this->start;
    //   this->start = index + 1;
    //   return {{old_start, index}, {index + 1, this->end}};
    // } else if (this->end == index) {
    //   ll old_end = this->end;
    //   this->end = index - 1;
    //   return {{this->start, index}, {index + 1, old_end}};
    // } else {
    //   this->left = new RNode(this->start, index);
    //   this->right = new RNode(index + 1, this->end);
    //   return {{this->start, index}, {index + 1, this->end}};
    // }
    // auto new_ranges = ranges.split(destroyed_coach);

    auto rr = rang.upper_bound({destroyed_coach, destroyed_coach});
    cout << rr->first << " " << rr->second << endl;
    pair<pair<ll, ll>, pair<ll, ll>> new_ranges = {{0, n}, {n, n}};
    auto left_range = new_ranges.first;
    auto right_range = new_ranges.second;

    if (left_range.first == left_range.second &&
        right_range.first == right_range.second) {
      chaos -= round_up(train[destroyed_coach]);
      segments--;
    } else if (left_range.first == left_range.second) {
      ll original = calculated[{left_range.first, right_range.second}];
      chaos -= round_up(original);
      ll s = original - train[destroyed_coach];
      calculated[right_range] = s;
      chaos += round_up(s);
    } else if (right_range.first == right_range.second) {
      ll original = calculated[{left_range.first, right_range.second}];
      chaos -= round_up(original);
      ll s = original - train[destroyed_coach];
      calculated[left_range] = s;
      chaos += round_up(s);
    } else {
      ll original = calculated[{left_range.first, right_range.second}];
      chaos -= round_up(original);
      ll l = seg_tree.query(left_range.first, left_range.second);
      calculated[left_range] = l;
      ll r = original - l - train[destroyed_coach];
      calculated[right_range] = r;
      chaos += round_up(l) + round_up(r);
      segments++;
    }

    max_chaos = max(max_chaos, chaos * segments);
  }

  cout << max_chaos << endl;
}
