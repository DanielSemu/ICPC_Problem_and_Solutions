#include <bits/stdc++.h>
using namespace std;
int main(){
int i,j,t;
long long a,b,c,max;
cin>>t;
while(t--){
cin>>a;
max=a;
cin>>b;
if(b>max)
max=b;
cin>>c;
if(c>max)
max=c;
if(a==b && b==c)
cout<<1<<" "<<1<<" "<<1<<endl;
else {

a=max-a;
if(a!=0)
a++;
b=max-b;
if(b!=0)
b++;
c=max-c;
if(c!=0)
c++;
cout<<a<<" "<<b<<" "<<c<<endl;
}
}
}