#include <bits/stdc++.h>
using namespace std;
bool isPrime(int n){
	if (n<=1){
		return false;
	}
	else{
		for (int i=0; i*i <=n; i++){
		if(n%i==0){
			return false;
		}
	return true;
	}
	}
	
	
}
int main(){
int x; cin>>x;
	while(x!=-1){	
	
	if(x==-1)
		break;
	bool t = isPrime(x);
	if(t){
		cout<<x<<" is PRIME!!\n";
	}
	else{
		cout<<x<<" is COMPOSITE TT\n";
	}
	cin>>x;
	}
	

	
	return 0;
	
}
