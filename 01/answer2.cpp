#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
	ifstream infile("input.txt");
	unordered_set<int> asdf;
	vector<int> arr;

	int cur;
	while (infile >> cur) {
		asdf.insert(cur);
		arr.push_back(cur);
	}

	for (auto i=arr.begin(); i!=arr.end(); i++) {
		for (auto j=arr.begin(); j!= arr.end(); j++) {
			if (asdf.find(2020 - *i - *j) != asdf.end()) {
         	cout << "found: " << *i << ", " << *j << ", " << 2020-*i-*j << endl;
				cout << "* = " << *i**j*(2020-*i-*j) << endl;
				return 0;
			}
		}
	} 

	return 0;
}
