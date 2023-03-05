#include <bits/stdc++.h>

using namespace std;

#define all(c) begin(c), end(c)
#define ssize(c) (int)c.size()
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vll = vector<ll>;

bool dig(ll n, ll m, ll ln, ll lm) {
  if (!n && ln > 1)
    return false;
  if (!m && lm > 1)
    return false;

  set<ll> dig;
  ll tn = 0, tm = 0;
  while (n) {
    if (dig.find(n % 7) != dig.end())
      return false;
    dig.insert(n % 7);
    n /= 7;
    tn++;
  }

  if (tn < ln) {
    if (dig.find(0) != dig.end())
      return false;
    dig.insert(0);
  }

  while (m) {
    if (dig.find(m % 7) != dig.end())
      return false;
    dig.insert(m % 7);
    m /= 7;
    tm++;
  }

  if (tm < lm)
    if (dig.find(0) != dig.end())
      return false;

  return true;
}

ll len(ll n) {
  ll r = 0;
  while (n)
    r++, n /= 7;
  return r;
}

int main() {
  cin.tie(0)->sync_with_stdio(false);

  ll n, m;
  cin >> n >> m;

  ll ln = len(n), lm = len(m);
  if (ln + lm > 7)
    cout << 0 << endl;
  else {
    ll res = 0;
    for (int h = 0; h < n; h++)
      for (int k = 0; k < m; k++)
        if (h != k && dig(h, k, ln, lm))
          res++;
    cout << res;
  }
}
