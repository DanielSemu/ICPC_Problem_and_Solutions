#include<bits/stdc++.h>
using namespace std;
int main(){
	string x;
	cin>>x;
	int k=0,d;
	d=sqrt(x.size());
	 char arr[d][d];
	
	for(int i=0; i<d; i++){
		for(int j=0; j<d; j++){
			arr[i][j]=x[k];
			k+=1;
		}
	}
	for(int i=d-1; i>=0;i--){
		for(int j=0; j<d; j++){
			cout<<arr[j][i];
		}
	}
	
	
	
	return 0;
}
