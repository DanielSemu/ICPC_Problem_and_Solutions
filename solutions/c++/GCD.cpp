#include <bits/stdc++.h>
using namespace std;
int gcd (int a, int b) {
return b == 0 ? a : gcd(b, a % b);
}
int main(){
	long long int x,y,gg,ll;
	while(true){
		cin>>x;
		if(x== -1){
			break;
		}
		cin>>y;
		 gg=gcd(x,y);
		 ll=(x*y)/gg;
		 cout<<gg<<" "<<ll<<endl;
	}
}
