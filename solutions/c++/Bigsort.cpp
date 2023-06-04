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
	for(int i=0; i<t; i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}
}
