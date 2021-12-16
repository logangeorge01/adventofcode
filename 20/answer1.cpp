#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <unordered_set>
#include <vector>

using namespace std;

map<string, int> m;


int c=0;
void check(string word, int tile) {
	string cp = word;
	reverse(cp.begin(), cp.end());
	if (m.find(word) == m.end() && m.find(cp) == m.end())
		m.insert(pair<string, int>(word, tile));
	else {
		m.erase(word);
		m.erase(cp);
	}
}

int main() {
	ifstream infile("input.txt");

	string b,e,word;
	int i=0,tile;
	while (infile >> word) {
		if (!i) {
			i++;
			continue;
		}
		if (i==1) {
			tile=stoi(word.substr(0,4));
			i++;
			continue;
		}
		b.push_back(word[0]);
		e.push_back(word[9]);

		if (i==2 || i==11) {
			check(word, tile);
			if (i==11) {
				check(b, tile);
				check(e, tile);
				e.clear();
				b.clear();
				i=0;
				c++;
				continue;
			} 
		}
		i++;
	}

	vector<int> v;
	unordered_set<int> s;
	for (auto i=m.begin(); i!=m.end(); i++) {
		if (s.find(i->second) != s.end()) v.push_back(i->second);
		else (s.insert(i->second));
	}

	cout << v[0] << " " << v[1] << " " << v[2] << " " << v[3] << endl;

	return 0;
}
