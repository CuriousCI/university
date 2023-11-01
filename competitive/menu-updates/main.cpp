#include <bits/stdc++.h>

using namespace std;
using ll = long long;


int main() {
    cin.tie(0)->sync_with_stdio(false);

    ll days, updates;
    cin >> days >> updates;

    queue<pair<ll, ll>> removed;
    priority_queue<ll, vector<ll>, greater<ll>> ready_queue;
    ll top_item = 1;

    for (ll day = 0; day < updates; day++) {
        char action;
        cin >> action;

        while (removed.size() && removed.front().second + days <= day) {
            ready_queue.push(removed.front().first);
            removed.pop();
        }

        if (action == 'r') {
            ll code;
            cin >> code;
            removed.push({code, day});
        } else if (ready_queue.size()) {
            ll ready_code = ready_queue.top();
            ready_queue.pop();
            cout << ready_code << endl;
        } else {
            cout << top_item << endl;
            top_item++;
        }
        
    }
}
