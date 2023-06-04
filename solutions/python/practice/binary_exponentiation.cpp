#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int mod=1e9 + 7;
ll modular(int base , int expo){

    if(expo == 0)
    return 1;
    ll result=modular(base ,expo/2);
    if(expo %2 ==1)
    return (((result * result)%mod) *base)%mod;
    else
    return (result * result)%mod;
}
// void Binary(double a, ll b){
//     double res=1.0;
//     if(b<0)b=-1*b;
//     while(b>0){
//         if(b%2==1){
//             res*=a;
//             b--;
//         }
//         else{
//             a*=a;
//             b=b/2;
//         }
//     }
//     if(b<0) res=(double)(1.0)/(double)(res);
//     cout<<res<<endl;
// }
int main(){

ll b,s;
cin>>s;
while(s--){
double a;
cin>>a>>b;
cout<<modular(a,b)<<endl;
}
//Binary(a,b);

}

// #include<bits/stdc++.h>
// using namespace std;

// int main(){
 
//  int a,x,y,z;
//  cin>>a;
//  while(a--){
//      cin>>x>>y>>z;
//      int res=((4*x)+(2*y));
//      cout<<res<<endl;
//  }
    
//  return 0;
 
// }
