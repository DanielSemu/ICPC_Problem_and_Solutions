#include <bits/stdc++.h>
using namespace std;
int main(){
	long long int a, b,c,lmab,LCM;
	while(1){
		cin>>a;
		if(a == -1){
			break;
		}
		cin>>b>>c;
		lmab=(a*b)/__gcd(a,b);
		LCM=(c* lmab)/__gcd(c,lmab);
		cout<<LCM<<endl;
	}
	
	
	
	return 0;
}
