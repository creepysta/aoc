#include <bits/stdc++.h>
using namespace std;

vector<int> a;
int n;

void one() {
	int low = 0, high = n-1;
	while(low < high) {
		int now = a[low] + a[high];
		if(now < 2020)
			low ++;
		else if (now > 2020)
			high --;
		else {
			cout << a[low] * a[high] << endl;
			break;
		}
	}
}

void two() {
	for(int i = 0; i < n; i++) {
		int low = i + 1, high = n-1;
		while(low < high) {
			int now = a[i] + a[low] + a[high];
			int64_t mul = a[i] * a[low] * a[high];
			if(now == 2020) {
				cout << mul << endl;
				return;
			} else if (now < 2020)
				low++;
			else
				high--;
		}
	}
}

int main() {
	int x;
	while(cin >> x) {
		a.push_back(x);
	}
	sort(a.begin(), a.end());
	n = a.size();
	one();
	two();
	return 0;
}
