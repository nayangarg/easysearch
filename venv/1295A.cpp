#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;

	while (t--)
	{
		int n;
		cin >> n;

		while (n > 3)
		{
			cout << 1;
			n -= 2;
		}

		if (n==3)
		{
			cout << "7\n";
		}
		else
		{
			cout << "1\n";
		}
	}

	return 0;
}
