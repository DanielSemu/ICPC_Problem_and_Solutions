#include <bits/stdc++.h>
using namespace std;
int main(){
	const int M=1000000007;
	long long int t,num,power,res,total=0;
	cin>>t;
	for(int j=1; j<=t; j++){
		total=0;
	cin>>num>>power;
	for(int i=1; i<=num; i++)
	{
		if(num%i==0)
		{
			res=pow(i,power);
			total+=res;
		}
		
	}
	cout<<"Case "<<j<<": "<<total%M<<endl;
}
	return 0;
}


