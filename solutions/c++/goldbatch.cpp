#include <bits/stdc++.h>
using namespace std;
bool prime(int n)
{
    if((n==2)||n==3)
    return true;
    else{
    for (int i =2; i*i <= n; i++){
                if (n % i == 0) {
               return false;
    }}
    return true;
    }
}
int main(){
   
  while(1){
  int num,a,b;
     cin>>num;
     if(num==-1)
     break;
     else{
       a=num/2;
       b=num-a;
       while(a>=2){
       if (prime(a)){
            if(prime(b)){
             cout<<a<<" "<<b<<endl;   
             break;
       }else{
        a-=1;
        b+=1;
       }
                                                           
       }else{
         a-=1;
        b+=1;
       }
       }
     }
  }
}