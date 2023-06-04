#include<bits/stdc++.h>
using namespace std;
int main(){
long long int a,it=0;

cin>>a;
vector<long long int>div;
if(a==1)cout<<1<<endl;
else{
for(long long int i=1; i<=sqrt(a); i++){
    if(a%i==0){
        if(i != a/i){
        div.push_back(i);
        div.push_back(a/i);
        }
        else{
           div.push_back(i); 
        }
    
    }
} 
sort(div.begin(), div.end());
for(auto i : div)
    cout<<i<<endl;
}
    return 0;
}