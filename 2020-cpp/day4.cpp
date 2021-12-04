#include <bits/stdc++.h>
using namespace std;

vector<string> a;
vector<vector<pair<string, string>>> tokens;
int n;

void tokenise() {
	for(string line : a) {
		stringstream ss(line);
		string key, token, val;
		vector<pair<string, string>> toks;
		while(ss >> token) {
			int pos = token.find(':');
			key = token.substr(0, pos);
			val = token.substr(pos+1);
			//cout << key << '$' << val << endl;
			toks.push_back({key, val});
		}
		tokens.push_back(toks);
	}
}

void parse() {
	string s, pass = "";
	while(getline(cin, s)) {
		if (s.length() == 0) {
			a.emplace_back(pass);
			pass = "";
		}
		if (pass.length())
			pass += " " + s;
		else
			pass = s;
	}
	if (pass.length()) {
		a.emplace_back(pass);
	}
	n = a.size();
	tokens.reserve(n);
	tokenise();
}


void one() {
	int ans = 0;
	for(auto elem : tokens) {
		unordered_set<string> u{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
		for(auto e : elem) {
			if(e.first != "cid")
				u.erase(e.first);
		}
		if(u.size() == 0)
			ans ++;
	}
	cout << ans << '\n';
}

void two() {
	int ans = 0;
	for(auto elem : tokens) {
		unordered_set<string> u{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
		bool valid = true;
		for(auto e : elem) {
			string key = e.first, val = e.second;
			if(key != "cid")
				u.erase(key);
			if (key == "byr") {
				valid &= val.length() == 4 && (stoi(val) <= 2002 && stoi(val) >= 1920);
			} else if(key == "iyr") {
				valid &= val.length() == 4 && (stoi(val) <= 2020 && stoi(val) >= 2010);
			} else if(key == "eyr") {
				valid &= val.length() == 4 && (stoi(val) <= 2030 && stoi(val) >= 2020);
			} else if(key == "hgt") {
				bool cmin = val.substr(val.length()-2) == "cm";
				int height = -1;
				if(cmin)
					height = stoi(val.substr(0, val.find('c')));
				else 
					height = stoi(val.substr(0, val.find('i')));
				valid &= cmin ? (height >= 150 && height <= 193) : (height >= 59 && height <= 76);
				//cout << cmin << ' ' << valid << ' ' << height << endl;
			} else if(key == "hcl") {
				valid &= val[0] == '#';
				string code = val.substr(1);
				valid &= code.length() == 6;
				for(char c : code) {
					valid &= (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f');
				}
			} else if(key == "ecl") {
				unordered_set<string> eye{"amb","blu","brn","gry","grn","hzl","oth"};
				valid &= eye.find(val) != eye.end();

			} else if(key == "pid") {
				valid &= val.length() == 9;
				for(char c : val)
					valid &= (c >= '0' && c <= '9');
			}
		}
		if(u.size() == 0 && valid)
			ans ++;
	}
	cout << ans << '\n';
}

int main() {
	parse();
	one();
	two();
	return 0;
}
