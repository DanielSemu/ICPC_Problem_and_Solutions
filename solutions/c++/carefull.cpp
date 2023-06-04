#include <bits/stdc++.h>
using namespace std;
int main(){
	long long int x,y,z,t;
	while(true){
	
	cin>>t;
	if(t== -1)
	break;
	
	cin>>y>>z;
	t = t%pow(10,9);
	y = y%pow(10,9);
	cout<<((t%z)*(y%z))%z<<endl;
	
	
}
	
	
	return 0;
}
