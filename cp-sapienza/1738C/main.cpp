#include <bits/stdc++.h>
#include <utility>

using namespace std;

#define all(c) begin(c), end(c)
#define ssize(c) (int)c.size()
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vll = vector<ll>;

int main() {
  ll t;
  cin >> t;
  while (t--) {
    ll n;
    cin >> n;

    ll odd = 0, even = 0, m;
    while (n--) {
      cin >> m;
      if (m & 1)
        odd++;
      else
        even++;
    }

    // Reduce to base case!
    odd %= 4;
    even %= 4;

    if (odd == 0) {
      cout << "Alice" << endl;
    } else if (odd == 1) {
      cout << ((even & 1) ? "Alice" : "Bob") << endl;
    } else if (odd == 2) {
      cout << "Bob" << endl;
    } else if (odd == 3) {
      cout << "Alice" << endl;
    }
  }
}
