#include <bits/stdc++.h>
using namespace std;

vector<string> g;
int n, m;

void one() {
	int64_t mul = 1;
	vector<pair<int, int>> p{{1,1},{1,3},{1,5},{1,7},{2,1}};
	for (auto d : p) {
		int trees = 0;
		for(int i = d.first, j = d.second; i < n; i += d.first, j = (j+d.second) % m) {
			if (g[i][j] == '#') {
				trees ++;
			}
		}
		mul *= trees;
	}
	cout << mul << endl;
}

int main() {
	string s;
	while(cin >> s) {
		g.emplace_back(s);
	}
	n = g.size(), m = g[0].size();
	one();
	return 0;
}
