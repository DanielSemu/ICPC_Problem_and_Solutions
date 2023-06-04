#include <bits/stdc++.h>
using namespace std;
int main(){
	 double t, AC,BC,r;
	while(true){
		cin>>t;
		if(t==-1)
		break;
		cin>>r;
		AC=r* cos(t);
		BC=r* sin(t);
		fprintf(stdout, "%.5f",AC);
		cout<<" ";
		fprintf(stdout, "%.5f",BC);
		cout<<endl;
		
	}
	
}
