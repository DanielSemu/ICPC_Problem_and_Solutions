#include <bits/stdc++.h>
using namespace std;
int main(){
float p,q,d;
float div;

while(1){
    cin>>p;
	if(p==-1)
	break;
cin>>q>>d;	
div=p/q;
cout<<fixed<<setprecision(d) << div <<endl;

}


return 0;	
}


