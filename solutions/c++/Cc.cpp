#include <bits/stdc++.h>
using namespace std;
int main(){
int x;
cin>>x;
cout<<x<<" ";
while(1){
	if(x==1)
	break;
	if(x%2==0){
		x=x/2;
	}
	else{
		x=3*x +1;
		
	}
	cout<<x<<" ";
	if(x==1)
	break;
}
cout<<endl;	
return 0;
}
