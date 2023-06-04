#include <bits/stdc++.h>
using namespace std;

int main() {
 string s;
 cin>>s;
    
    char p[s.length()];
 
    int i,co=0;
    for (i = 0; i < sizeof(p); i++) {
        p[i] = s[i];
    }
   for (i=0;i<s.length();i++){
   	if(count(p,p+sizeof(p), p[i])>1){
   		co=1;
	   }
   }
if(co==1){
	cout<<0<<endl;
}
else
cout<<1<<endl;
return 0;	
}
