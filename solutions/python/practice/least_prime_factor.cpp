#include<bits/stdc++.h>
using namespace std;
void leastprime(int n){
    vector<int>L_factor(n+1 ,0);
    L_factor[1]=1;
    for(int i=2; i<=n; i++){
        if(L_factor[i]==0){
            L_factor[i]=i;
            for(int j=i*i; j<=n; j+=i){
                if(L_factor[j]==0){
                    L_factor[j]=i;
                }
            }
        }
    }
    for(int i=1; i<=n; i++){
        cout<<i<<":"<<L_factor[i]<<" ";
    }
    cout<<endl;

}
int main(){
    int t,n;
    cin>>t;
    while (t--){
        cin>>n;
        leastprime(n);
    }


    return 0;
}