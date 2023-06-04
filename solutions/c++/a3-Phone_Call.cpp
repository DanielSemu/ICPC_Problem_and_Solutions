
#include<iostream>
using namespace std;
int main(){
long long min1,min2_10,min11,s;
cin>>min1>>min2_10>>min11>>s;
int t=0,i=1;
while(s>0){

if(i==1){
    s-=min1;
    if(s>=0)
    t++;
}

else if(i>=2 && i<=10){
    s-=min2_10;
    if(s>=0)
    t++;
}
else if(i>10){
    s-=min11;
    if(s>=0)
    t++;
}

i++;
}
cout<<t;
return 0;
}