#include <iostream>
using namespace std;
int main()
{
	long long int n, total=0,each;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		each=4*(i);
		total+=each;
	}
	cout<<total<<endl;
	
}
