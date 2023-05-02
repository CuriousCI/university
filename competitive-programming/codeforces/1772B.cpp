#include <iostream>

using namespace std;

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        bool h = (a < b && c < d) || (a > b && c > d);
        bool v = (a < c && b < d) || (a > c && b > d);

        cout << (h && v ? "YES" : "NO") << endl;
    }
}
