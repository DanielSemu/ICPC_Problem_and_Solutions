#include <bits/stdc++.h>
using namespace std;
int main(){
	int x,y,sum=0;
	cin>>x;
	while(x>0){
		cin>>y;
		int arr[y];
		for(int i=0; i<y; i++){
			cin>>arr[i];
			sum+=arr[i];
		}
		if(sum %y ==0){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
		x--;
	}

return 0;
}
