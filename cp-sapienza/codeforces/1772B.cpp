#include <iostream>

using namespace std;

int main() {

    int t; 
    cin >> t;
    while(t--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        cout << ((a < b && c < d && a < c && b < d) || (a > b && c > d && a > c && b > d) ? "YES" : "NO") << endl;
    }
}
