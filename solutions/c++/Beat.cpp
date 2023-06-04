#include <bits/stdc++.h>
using namespace std;
int main() {
	long long int x,y,a,b,t;
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>a>>b;
		if(a<b){
			cout<<"impossible"<<endl;
		}
		else{
			if((a%2== 1 && b%2==0)||(a%2== 0 && b%2==1)){
					cout<<"impossible"<<endl;
			}
			else{
				x=(a+b)/2;
				y=a-x;
				if(x>=0 && y>=0){
						if(x>y)
							cout<<x<<" "<<y<<endl;
						else
							cout<<y<<" "<<x<<endl;
							}
				else{
					cout<<"impossible"<<endl;
				}
				}
			}
			
		}
	
	
return 0;	
}
	

