#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,a,odd,even;
	cin>>t;
	while(t--){
	    cin>>a;
        odd=(a+1)/2;
        even=a/2;
	    cout<<odd*even*2<<endl;
	}
	return 0;
}
