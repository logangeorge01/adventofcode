#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream infile("input.txt");

	string line;
	int ret[5]={0}, i[4]={0};
	int d=0;

	while (infile >> line) {
		//cout << "d: " << d << ", i[0]: " << line[i[0] % line.size()] << endl;
		if (!(d % 2) && line[(i[0]/2) % line.size()] == '#') {
			ret[4]++;
		}
		d++;
		for (int j=0; j<4; j++) {
			if (line[i[j] % line.size()] == '#') ret[j]++;
			i[j] += (j*2)+1;
		}
	}
	long asdf=ret[0];
	for (int j=1; j<5; j++) asdf*=ret[j];
	cout << asdf << endl;

	return 0;
}
