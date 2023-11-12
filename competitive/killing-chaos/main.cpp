#include <algorithm>
#include <iostream>
#include <limits>
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

ll round_up(ll number) {
  ll remainder = number % 10;
  return remainder ? number + (10 - remainder) : number;
}

int main() {
  cin.tie(0)->sync_with_stdio(false);
  ll number_of_coaches;
  cin >> number_of_coaches;

  vector<ll> train;
  for (ll _ = 0; _ < number_of_coaches; _++) {
    ll coach;
    cin >> coach;
    train.push_back(coach);
  }

  auto segment_tree = SegmentTree(train);

  ll max_chaos = round_up(segment_tree.query(0, number_of_coaches)),
     chaos = max_chaos;
  set<pair<ll, ll>> segments{{0, number_of_coaches}};

  for (ll _ = 0; _ < number_of_coaches; _++) {
    ll destroyed_coach;
    cin >> destroyed_coach;
    destroyed_coach--;

    auto segment = *segments.upper_bound({0, destroyed_coach});
    if (segment.second <= destroyed_coach)
      segment = *segments.lower_bound({destroyed_coach, 0});

    if (destroyed_coach == segment.first &&
        destroyed_coach + 1 == segment.second) {
      chaos -= round_up(train[destroyed_coach]);
    } else if (destroyed_coach == segment.first) {
      chaos -= round_up(segment_tree.query(segment.first, segment.second));
      chaos +=
          round_up(segment_tree.query(destroyed_coach + 1, segment.second));
      segments.insert({destroyed_coach + 1, segment.second});
    } else if (destroyed_coach + 1 == segment.second) {
      chaos -= round_up(segment_tree.query(segment.first, segment.second));
      chaos += round_up(segment_tree.query(segment.first, destroyed_coach));
      segments.insert({segment.first, destroyed_coach});
    } else {
      chaos -= round_up(segment_tree.query(segment.first, segment.second));
      chaos += round_up(segment_tree.query(segment.first, destroyed_coach));
      chaos +=
          round_up(segment_tree.query(destroyed_coach + 1, segment.second));

      segments.insert({segment.first, destroyed_coach});
      segments.insert({destroyed_coach + 1, segment.second});
    }
    segments.erase(segment);
    for (auto s : segments)
      cout << "(" << s.first << ";" << s.second << ") ";
    cout << endl;
    max_chaos = max(max_chaos, (ll)(chaos * segments.size()));
  }

  cout << max_chaos << endl;
}
