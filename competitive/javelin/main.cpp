#include <bits/stdc++.h>

using namespace std;

int main() {
    int rods = 0;
    cin >> rods;

    int total = 1;
    while (rods--) {
        int rod;
        cin >> rod;
        total += rod - 1;
    }

    cout << total;
}
