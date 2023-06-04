#include <bits/stdc++.h>
using namespace std;
int main() {
int n;
cin >> n;
// Store the sequence in a vector
vector<int> S(n);
for (int i = 0; i < n; ++i) cin >> S[i];
// Calculate the minimum value
int m = S[0];
for (int i = 1; i < n; ++i) {
if (S[i] < m) m = S[i];
}
// Write the normalized sequence
cout << n;
 for (int i = 0; i < n; ++i) cout <<  " " << S[i] - m;
cout << endl;
}
