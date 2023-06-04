#include <bits/stdc++.h>
using namespace std;
int main(){
long long int i,sum=0,n;
cin>>n;
for(i=1; i<=n;i++){
	sum+=(i*i*i);
}
cout<<sum;
return 0;}

