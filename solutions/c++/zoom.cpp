#include <bits/stdc++.h>
using namespace std;
int main(){
  string m;
  cin>>m;
  string tm = "";
  int l = m.length();
  for (int i=0; i<l-1; i++){
    if(m[i]== m[i+1]){
      tm= tm+"M";
      i++;
    }
    else{
      tm= tm+m[i];
    }
  }
  
  cout<<tm;
  
  
  return 0;
}


