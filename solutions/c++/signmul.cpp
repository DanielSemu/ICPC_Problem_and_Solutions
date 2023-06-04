#include <bits/stdc++.h>
using namespace std;
int main()
{	
long long int t, p=1, q=1;
		cin>>t;
	while(true){
	
		long long int ar[t], ar2[t];
		p=1, q=1;
		for (long long int v =0; v<t; v++){
			cin>>ar[v]>>ar2[v];
		}
		for (long long int i=ar[0]; i<=ar2[0]; i++){
			if(ar[0]==ar2[0]){
				p = ar[0];
			}
			else{
			p = p*i;
			}
			
			
		}
		for (long long int i=ar[1]; i<=ar2[1]; i++){
				if(ar[0]==ar2[0]){
				q = ar[0];
			}
			else{
		q = q*i;
			}
			
		}
		if((q*p)<0){
			cout<<"-"<<endl;
		}
		else if((q*p)>0){
			cout<<"+"<<endl;
		}
		else{
			cout<<"0"<<endl;
		}
		cin>>t;
		if(t==-1){
			break;
		}
	}
}

