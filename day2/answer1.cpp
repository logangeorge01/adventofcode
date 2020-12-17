#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream infile("input.txt");

	int min, max, cur, ret=0;
	char letter, t;
	string line, pass;
	
	while (infile >> min >> t >> max >> letter >> t >> pass) {
		cur=0;
		for (int i=0; i<pass.size(); i++) {
			if (pass[i]==letter) cur++;
		}
		if (cur <= max && cur >= min) ret++;
	}

	cout << ret << endl;

	return 0;
}
