#include <bits/stdc++.h>
using namespace std;
int main(){
	char A,B,C;
	int arr[3];
	for(int i=0; i<3; i++){
		cin>>arr[i];
	}
		for(i = 0; i<3; i++) {
   for(j = i+1; j<3; j++)
   {
      if(arr[j] < arr[i]) {
         temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;
      }
   }
}
 A=
	
	return 0;
}
