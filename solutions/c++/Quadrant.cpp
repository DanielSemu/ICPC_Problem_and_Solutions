
#include <bits/stdc++.h>
#define lli long long int
#define PI 3.14159265
using namespace std;
int main(){
  while (1){

  lli a,b;
  cin>>a;
   float c= (PI/180)*a;
  if (a==-1){
    break;
  }  
  cin>>b;
  float ac= cos(c)*b;
  float bc= sin(c)*b;
  cout << fixed << setprecision(5) <<ac<<" "<<bc<<endl;
  }  
}
