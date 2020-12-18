#include <iostream>

using namespace std;

// 0 inactive, 1 active, 2 active was inactive, 3 inactive was active

int arr[25][25][25] = {0};

void dopoint(int i, int j, int k) {
	int nactive=0;
	for (int z=max(i-1,0); z<=min(i+1,24); z++) {
		for (int y=max(j-1,0); y<=min(j+1,24); y++) {
			for (int x=max(k-1,0); x<=min(k+1,24); x++) {
				if (z==i && y==j && x==k) continue;
				if (arr[z][y][x]%2) nactive++;
			}
		}
	}
	if (arr[i][j][k] && nactive!=2 && nactive!=3) arr[i][j][k]=3;
	else if (!arr[i][j][k] && nactive==3) arr[i][j][k]=2;
}

void cycle(int r) {
	if (r>1) cycle(r-1);
	for (int i=0; i<25; i++) {
		for (int j=0; j<25; j++) {
			for (int k=0; k<25; k++) {
				dopoint(i, j, k);
			}
		}
	}
	for (int i=0; i<25; i++) {
		for (int j=0; j<25; j++) {
			for (int k=0; k<25; k++) {
				if (arr[i][j][k]==2) arr[i][j][k]=1;
				if (arr[i][j][k]==3) arr[i][j][k]=0;
			}
		}
	}
}

int main() {
	arr[13][10][10] = 1;
arr[13][10][11] = 1;
arr[13][10][15] = 1;
arr[13][10][17] = 1;

arr[13][11][10] = 1;
arr[13][11][13] = 1;
arr[13][11][14] = 1;
arr[13][11][17] = 1;

arr[13][12][12] = 1;
arr[13][12][14] = 1;
arr[13][12][15] = 1;
arr[13][12][16] = 1;
arr[13][12][17] = 1;

arr[13][13][11] = 1;
arr[13][13][14] = 1;

arr[13][14][10] = 1;
arr[13][14][11] = 1;
arr[13][14][12] = 1;
arr[13][14][13] = 1;
arr[13][14][14] = 1;
arr[13][14][15] = 1;
arr[13][14][16] = 1;
arr[13][14][17] = 1;

arr[13][15][10] = 1;
arr[13][15][11] = 1;
arr[13][15][12] = 1;
arr[13][15][13] = 1;
arr[13][15][14] = 1;
arr[13][15][15] = 1;
arr[13][15][17] = 1;

arr[13][16][11] = 1;
arr[13][16][12] = 1;
arr[13][16][13] = 1;
arr[13][16][14] = 1;
arr[13][16][17] = 1;

arr[13][17][11] = 1;
arr[13][17][12] = 1;
arr[13][17][13] = 1;
arr[13][17][15] = 1;

	for (int j=0; j<25; j++) {
		for (int k=0; k<25; k++) {
			cout << (arr[13][j][k] ? "#" : ".");
		}
		cout << endl;
	}
	cout << endl << endl << endl;

	cycle(6);
	int active=0;
	for (int i=0; i<25; i++) {
		for (int j=0; j<25; j++) {
			for (int k=0; k<25; k++) {
				if (arr[i][j][k]) active++;
			}
		}
	}
	cout << "active: " << active << endl;

	return 0;
}
