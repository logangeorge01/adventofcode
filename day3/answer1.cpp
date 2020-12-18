#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream infile("input.txt");

	string line;
	int ret=0, i=0;

	while (infile >> line) {
		if (line[i % line.size()] == '#') ret++;
		i+=3;
	}

	cout << ret << endl;

	return 0;
}
