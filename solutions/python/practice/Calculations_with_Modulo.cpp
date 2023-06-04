#include<bits/stdc++.h>
using namespace std;
// int modpow(long int x,long long int n,long long int m) {
// if (n == 0) return 1%m;
// int u = modpow(x,n/2,m);
// u = (u*u)%m;
// if (n%2 == 1) u = (u*x)%m;
// return u;
// }
int power(int a , int n){
    int res=1;
    while(n){
        if(n%2)
        res*=a ,n--;
        else
        a*=a ,n/=2;
    }
    return res;
}
int main()
{
   // int A, B, C, M,res1,res2,res3,res4;
   long long int x, y ,p=10000000 ;
    cin>>x>>y;
    cout<<power(x,y)<<endl;
    cout<<pow(x,y)<<endl;
    // cout << "Power is " << modpow(x, y, p)<<endl;
    
    // binaryExponentiation(A,B);
    
return 0;
}