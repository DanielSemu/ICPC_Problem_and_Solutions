#include <bits/stdc++.h>
using namespace std;
int main(){
int n,s,k,m,min, max;

cin>>n>>s>>k>>m;

if (n<=s){
	min = m;
	max = ((n*(k+1))*m);
}
else{
	int num = n/s;
	int rem = n%s;
	if(rem >0){
		min = m*(num+1);
		max = k*m + min;
	}
	else{
		min = m*num;
		max = k*m +min;
	}
}

cout<<min<<" "<<max<<endl;
	return 0;
}
