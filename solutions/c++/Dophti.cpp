#include <bits/stdc++.h>
using namespace std;
int main(){
	long long int a, b,c,d;
	cin>>d;
	for(int i=1; i<=d; i++){
		cin>>a>>b>>c;
		 if (c% __gcd(a,b)==0)
        cout<<"Case "<< i << ": Yes"<<endl;
    else
         cout<<"Case "<< i << ": No"<<endl;
    
		
	}
return 0;	
}


