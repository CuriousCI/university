#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
	ll t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;

		auto a = vector<ll>(n);
		for (auto &i : a)
			cin >> i;

		ll M = LLONG_MAX, m = a[0];
		for (int i = 0; i < n - 1; i++)
		{
			if (a[i] < a[i + 1])
				m = min(a[i], m);
			else
				M = max(M, a[i]);
		}

		cout << (m > M ? M + 1 : -1) << endl;
	}
}