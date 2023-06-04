#include <bits/stdc++.h>
using namespace std;
int main(){
	int tt,t=1;
	string x;
	cin>>tt;
	float d,e,res;
	while(tt>0){
      	cin>>x;
	if(sizeof(x)==3){
		d=int(x[0]);
		res=d*05;
	}
	else{
		d=int(x[0]);
		e=int(x[4]);
		res=d*0.5 + e*0.05;
	}
		cout<<"Case "<<t<<": "<<res<<endl;
		tt--;
		t++;
	}
	
	
	
return 0;	
}
