#include <iostream>

using namespace std;

string test = "1 + (2 * 3) + (4 * (5 + 6))";

int main() {
	while (1) {
		try {
			int ret = stoi(test);
			cout << ret << endl;
			return 0;
		} catch(...) {
			int pos = test.find_last_of(')');
			while (pos>=0) {
				int i=pos;
				int a,b;
				while (test[i]!=')') {
					a=test[i+1] - 'A';
					b=test[i+5] - 'A';
					if (test[i+3]=='*') {
						test.replace(pos+1, 5, (a*b)+'A');
					} else {
						
					}
					i++;
				}
				//remove parens
			}
		}
	}

	return 0;
}
