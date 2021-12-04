/*
	author: Creepysta
	28-03-2021 12:32:02
*/
#include <bits/stdc++.h>
using namespace std;
const int MOD = int(1e9) + 7;
#define int int64_t
#ifdef LOCAL
#define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); cerr << "debug: [ "; err(_it, args); }
#else
#define debug(args...) 0;
#endif
#define tmpt template < class T
#define ostop ostream& operator<<(ostream& o
#define itfr { o << "[";for(auto e : x) o << e << ", "; o<<"\b\b]"; return o;}
void err(istream_iterator<string> it) { cerr << "\b\b ]\n";}
tmpt , class... Args>
void err(istream_iterator<string> it, T a, Args... args) { cerr << *it << ": "  << a << ", "; err(++it, args...); }
tmpt > ostop , const vector<T> &x) itfr
tmpt > ostop , const set<T> &x) itfr
tmpt , class V> ostop , const map<T,V> &x) itfr
tmpt , class V> ostop , const pair<T,V> &p) { o << "(";o << p.first << ", " << p.second << ")"; return o;}

vector<tuple<int, int, int, int>> classRange;
vector<pair<string, int>> names;
vector<int> whatiswhat;
vector<int> myTicket;
vector<vector<int>> tickets;
vector<bool> valid;
vector<vector<int>> workout;


ostream& operator << (ostream& out, const vector<int> &v) {
	for(int i : v) {
		out << i << ' ';
	}
	return out;
}


void parse(const string &filename) {
	//class rules
	string classline;
	ifstream ifs(filename);
	while(getline(ifs, classline) && classline.length()) {
		int t1, f1, t2, f2;
		int pos = classline.find(':');
		string name =classline.substr(0,pos);
		string need = classline.substr(pos+1);
		string mid = " or ";
		pos = need.find(mid);
		string beg = need.substr(0, pos), end = need.substr(pos + mid.length()-1);
		//cout << beg << ' ' << end << endl;
		pos = beg.find('-');
		t1 = stoi(beg.substr(0, pos));
		f1 = stoi(beg.substr(pos+1));
		pos = end.find('-');
		t2 = stoi(end.substr(0, pos));
		f2 = stoi(end.substr(pos+1));
		classRange.emplace_back(make_tuple(t1, f1, t2, f2));
		names.emplace_back(name, classRange.size()-1);
	}

	auto parseTicket = [&] (string ticket) {
		vector<int> tokens;
		int pos = -1, init = -1;
		//cout << ticket << endl;
		while((pos = ticket.find(',', init + 1)) != (int) string::npos) {
			string tok = ticket.substr(init+1, pos - init - 1);
			//cout << init << ' ' << pos << ' ' << tok;
			int num = stoi(tok);
			//cout << ' ' << num << endl;
			tokens.emplace_back(num);
			init = pos;
		}
		tokens.emplace_back(stoi(ticket.substr(init+1)));
		return tokens;
	};

	//my ticket
	string ticket;
	//Flush
	getline(ifs, ticket);
	getline(ifs, ticket);
	//cout << ticket << endl;
	myTicket = parseTicket(ticket);

	//other tickets
	string otherTicket;
	for(int i = 0; i < 2; i++)
		getline(ifs, otherTicket);
	while(getline(ifs, otherTicket)) {
		tickets.push_back(parseTicket(otherTicket));
	}


	// init
	whatiswhat.assign(classRange.size(), -1);
	workout.resize(tickets[0].size());
	valid.assign(tickets.size(), true);
}

bool interval(int a, int b, int x) {
	if(x >= a && x <= b)
		return true;
	return false;
}

struct forWhat {
	vector<int> classes;
	bool isValid;
};

forWhat checkInRange(int num) {
	forWhat fw = {vector<int>(), false};
	for(int i = 0; i < (int) classRange.size(); i++) {
		auto limit = classRange[i];
		int l1 = get<0>(limit),
			h1 = get<1>(limit),
			l2 = get<2>(limit),
			h2 = get<3>(limit);
		bool check = (interval(l1, h1, num) || interval(l2, h2, num));
		if(check) {
			fw.classes.push_back(i);
			fw.isValid = true;
		}
	}
	return fw; 
}


void one() {
	int64_t bad = 0;
	for(int i = 0; i < (int) tickets.size(); i++) {
		bool isok = true;
		for(int num : tickets[i]) {
			bool check = checkInRange(num).isValid;
			isok = check;
			if(!check)
				bad += num;
		}
		valid[i] = isok;
	}
	cout << bad << '\n';
}

void two() {
	// consider my ticket
	//tickets.push_back(myTicket);
	//valid.push_back(true);

	for(size_t tIdx = 0; tIdx < tickets.size(); tIdx++) {
		if(valid[tIdx]) {
			for(size_t pos = 0; pos < tickets[tIdx].size(); pos++) {
				int num = tickets[tIdx][pos];
				forWhat fw = checkInRange(num);
				//cout << "[" << tIdx << ' ' << pos << "]: " << fw.classes << endl;
				// vector of classes satisfying
				if(workout[pos].empty())
					workout[pos].assign(fw.classes.begin(), fw.classes.end());
				else {
					vector<int> res(classRange.size());
					sort(fw.classes.begin(), fw.classes.end());
					sort(workout[pos].begin(), workout[pos].end());
					auto it = set_intersection(
							fw.classes.begin(), fw.classes.end(),
							workout[pos].begin(), workout[pos].end(),
							res.begin()
							);
					res.resize(it - res.begin());
					//cout << "RES: " << res << endl;
					workout[pos].assign(res.begin(), res.end());
				}
			}
		}
	}
	int ws = workout.size();
	vector<int> pos(ws);
	for(int i = 0; i < ws; i++) {
		pos[i] = i;
	}
	sort(pos.begin(), pos.end(), [&](int a, int b) {
			return workout[a].size() < workout[b].size();
			});
	for(size_t pIdx = 0; pIdx < workout.size(); pIdx++) {
		debug(pos[pIdx], workout[pos[pIdx]])
	}
	for(auto e : names)
		debug(e)
	set<int> choices;
	for(int i = 0; i < 20; i++)
		choices.insert(i);

	int whs = whatiswhat.size();
	debug(pos[0], workout[pos[0]],choices)
	for(int i = 0; i < whs; i++) {
		ws = workout[pos[i]].size();
		int cls = 0;
		while(cls < ws && choices.find(workout[pos[i]][cls]) == choices.end())
			cls++;
		assert(choices.find(workout[pos[i]][cls]) != choices.end());
		whatiswhat[pos[i]] = workout[pos[i]][cls];
		choices.erase(choices.find(workout[pos[i]][cls]));
		debug(cls, pos[i], workout[pos[i]][cls],choices)
	}
	int64_t sum = 1;
	cout << "Classes: \n";
	for(int i = 0; i < 20; i++) {
		debug(pos[i], whatiswhat[pos[i]]);
	}
	vector<int> req;
	for(int i = 0; i < (int) names.size(); i++) {
		if(names[i].first.find("departure") != string::npos) {
			req.push_back(names[i].second);
		}
	}
	debug(myTicket, whatiswhat)
	for(int e : req) {
		debug(e,pos[e],whatiswhat[pos[e]], myTicket[whatiswhat[pos[e]]])
		sum *= myTicket[whatiswhat[pos[e]]];
	}
	cout << sum << endl;
}

signed main() {
#ifdef LOCAL
	parse("day16.in");
#else
	parse("day16.in");
#endif
	one();
	two();
	return 0;
}
