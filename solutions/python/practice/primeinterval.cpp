#include<bits/stdc++.h>
using namespace std;
#define ll long long int
bool isprime(int n){
   if(n<2)return false;
   for(int i=2; i*i<=n; i++)
    if(n%i==0)return false;
    return true; 
}
int main(){
    ll a,b,c,d;
    cin>>a;
    for (int i=0; i<a; i++){
        cin>>b>>c;
        for(b; b<=c; b++){
            if(isprime(b))
            cout<<b<<" ";
        }
        cout<<endl;
    }
    return 0;
}