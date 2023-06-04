# include<bits/stdc++.h>
using namespace std;
int main(){
	int t,n;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>n;
		int s[n],k=0,m=0;
		for(int i=0;i<n;i++){
			 cin>>s[i];
		}
		for(int i=1;i<n;i++){
			if(s[i]>s[i-1]){
				k++;
			}else if(s[i]<s[i-1]){
				m++;
			}
		}
		cout<<"Case "<<j<<": "<<k<<" "<<m<<endl;
	} 
	return 0;
}