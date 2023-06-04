#include<iostream>
using namespace std;
int main(){
    int i,j,n,sum=0,pro=0;
    cin>>n;
    int l[n],p[n];
    for(i=0;i<n;i++){
        cin>>l[i];
        sum+=l[i];
    }
    for(j=0;j<n;j++){
        cin>>p[j];
        pro+=l[j]*p[j];
    }
    cout<<sum<<" "<<pro;
    return 0;
}