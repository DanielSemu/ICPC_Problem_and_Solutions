#include<bits/stdc++.h>
using namespace std;
vector<int>prime1;
void isprime(){
    int n=90000000;
    bool arr[n+1];
    arr[0]=arr[1]=true;
    int p=2;
    for(int p=2; p*p<=n; p++){
        if(!arr[p]){
            for(int i=p*p; i<=n; i+=p){
                arr[i]=true;
            }
        }
    }
    for(int i=2; i<=n; i++){
        if(!arr[i])
        prime1.push_back(i);
    }
}

int main(){
    isprime();
    int n,num;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>num;
        cout<<prime1[num-1]<<endl;
    }
}