#include <bits/stdc++.h>
using namespace std;
int main() {
	long long int t, total =0, each=0;
	cin>>t;
	int a[t+1];
	for(int i=0; i<t; i++){
		total =0; each = 0;
		for (int i = 1; i<=t; i++){
	a[0] = 0;
	cin>>a[i];	
	}
	for (int i=1; i<=t; i++){
		each = 2*(pow(a[i],i));
		cout<<each<<endl;
		total = total + each;
		if( )
	}
	cout<<total<<endl;
		}
	return 0;
}

