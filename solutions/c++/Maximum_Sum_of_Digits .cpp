#include<bits/stdc++.h>
typedef long long int ll;

using namespace std;

ll foo(ll x)
{
    ll sum = 0;
    while(x){
        sum += (x%10);
        x/=10;
    }
    return sum;
}

int main()
{
    int i,j,k;
    ll n,m;
    cin>>n;
    if(n < 9){
        cout<<n;
        return 0;
    }
    ll x = 0;
    while(x*10+9<=n)
        x = x*10+9;

    cout<<foo(x)+foo(n-x);

    return 0;
}