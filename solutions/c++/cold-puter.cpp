#include<iostream>
using namespace std;
int main(){
	int x,count=0 ,num;
	cin>>x;
	for(int i=0; i<x; i++){
		cin>>num;
		if(num<0){
			count+=1;
		}
	}
	cout<<count;
	
	return 0;
}
