#include <bits/stdc++.h>
using namespace std;
int main(){
long long int t;
	
	while(true){
	
	cin>>t;
	if(t== -1)
	break;
	long long int arr[t];
	for(int i=0; i<t; i++){
		cin>>arr[i];
	}
	sort(arr, arr+t);
	long long int b[t/2];
	for(int i=0; i<t; i++){
		b[i]= arr[i+1]- arr[i];
	}	
	sort(b, b+(t/2));
	cout<<b[0]<<endl;
}
return 0;
}
