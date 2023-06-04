#include<bits/stdc++.h>
using namespace std;
int main(){
int n,x;
cin>>n;
vector<int>arr;
for(int i=0; i<n; i++){
    int j;
    cin>>j;
    arr.push_back(j);
}
sort(arr.begin() ,arr.end());
cin>>x;
for(int i=0; i<=n-3; i++){
  if((arr[i] +arr[i+1] +arr[i+2]) == x){
    cout<<arr[i]<<" "<<arr[i+1]<<" "<<arr[i+2]<<endl;
    break;
  }
}
    return 0;
}