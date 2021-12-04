#include <bits/stdc++.h>
using namespace std;

vector<string> inp;
vector<tuple<int, int, char, string>> a;
int n;
int cnt[26];

void parse() {
	for(string line : inp) {
		stringstream ss(line);
		string first, sec, thr;
		ss >> first >> sec >> thr;
		int dash = first.find('-');
		int f = stoi(first.substr(0, dash));
		int s = stoi(first.substr(dash+1));
		char c = sec.at(0);
		//cout << f << '$' << s << '$'<< c << '$' << thr << endl;
		a.emplace_back(make_tuple(f, s, c, thr));
	}
}


void one() {
	int ans = 0;
	for(int i = 0; i < n; i++) {
		int low = get<0>(a[i]), high = get<1>(a[i]);
		char c = get<2>(a[i]);
		string s = get<3>(a[i]);
		for(char cc : s)
			cnt[cc-'a']++;
		if(cnt[c - 'a'] >= low && cnt[c-'a'] <= high)
			ans++;
		memset(cnt, 0, sizeof cnt);
	}
	cout << ans << endl;
}

void two() {
	int ans = 0;
	for(int i = 0; i < n; i++) {
		int low = get<0>(a[i]), high = get<1>(a[i]);
		char c = get<2>(a[i]);
		string s = get<3>(a[i]);
		if (s[low-1] == c && s[high-1] != c) 
			ans ++;
		else if(s[low-1] != c && s[high-1] == c)
			ans ++;
	}
	cout << ans << endl;
}


int main() {
	string s;
	while(getline(cin, s)) {
		inp.emplace_back(s);
	}
	n = inp.size();
	a.reserve(inp.size());
	parse();
	memset(cnt, 0, sizeof(cnt));
	one();
	memset(cnt, 0, sizeof(cnt));
	two();
	return 0;
}
