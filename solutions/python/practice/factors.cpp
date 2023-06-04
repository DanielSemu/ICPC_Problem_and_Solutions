#include<bits/stdc++.h>
using namespace std;
int main(){
    int x;
    vector<int>factors;
    cin>>x;
    for(int i=1; i<=sqrt(x); i++){
        if(x%i==0){
            if(x/i==i){
            factors.push_back(i);
            }
            else
            {
            factors.push_back(i);
             factors.push_back(x/i);
            }
        }
    }
    sort(factors.begin(), factors.end());
    for(auto i : factors){
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}