#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int k, n;
		cin >> k >> n;

		auto m = 1, f = 1, d = n - k, a = 0;

		while (k--)
		{
			cout << m << ' ';
			if (a + f <= d)
			{
				a += f;
				f++;
			}
			else
				f = 1;
			m += f;
		}

		cout << endl;
	}
}