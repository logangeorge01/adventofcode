#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream infile("input.txt");

	int first, last, ret=0;
	char letter, t;
	string line, pass;
	
	while (infile >> first >> t >> last >> letter >> t >> pass) {
		if ((pass[first-1]==letter) != (pass[last-1]==letter)) ret++;
	}
	cout << ret << endl;

	return 0;
}
