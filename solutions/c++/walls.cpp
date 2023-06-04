#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int x,n, count,max;
	cin>>x;	
	
	for (int j=0; j<x; j++){
		cin>>n;
count=1;
int h[n];
	for (int i = 0 ; i<n; i++){
		cin>>h[i];
	}
	max = h[0];
	for (int i =1;i<n; i++){
		if((h[i]-h[i-1]>0)&&(max<h[i])){
			max=h[i];
			count++;
		}	
	}
	cout<<count<<endl;
	count=1;
		}	
return 0;	
}
