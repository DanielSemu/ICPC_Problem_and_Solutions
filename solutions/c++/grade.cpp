#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int x=9,i=1,j;
	float sum=0;
	char f;
	int arr[9];
	for(i;i<=9; i++){
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

	int temp;
	
	for(i = 3; i<10; i++) {
   for(j = i+1; j<10; j++)
   {
      if(arr[j] < arr[i]) {
         temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;
      }
   }
}
sum=arr[1]+arr[2]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9];
float av=sum/7;

    fprintf(stdout, "%.2f",av);
}
