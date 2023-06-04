#include <bits/stdc++.h>
using namespace std;
int main(){
		int x=6,i=1,j;
	float gpa=0;
	char f;
	int arr[7];
	for(i;i<=6; i++){
		cin>>f;
		if(f=='A'){
			arr[i]=4.0;
		}
		else if(f=='B'){
			arr[i]=3.0;
		}
	   	else if(f=='C'){
			arr[i]=2.0;
		}
	    else if(f=='D'){
			arr[i]=1.0;
		}
		else if(f=='F'){
		arr[i]=0;
		}
		else{
		arr[i]=0;
		}
	}
	gpa=((arr[1]*4)+ 3*(arr[2]+arr[3]+arr[4]+arr[5]+arr[6]));
	
	fprintf(stdout, "%.2f",gpa/19);
	
	return 0;
}

