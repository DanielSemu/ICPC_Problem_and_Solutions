#include<bits/stdc++.h>
using namespace std;
int main(){
    int x;
    int cou=1;
    cin>>x;
    for(int i=2; i<=int(sqrt(x)); i++){
        if(x%i==0)
        {
        cou=cou-1;
        cout<<"NOT PRIME!"<<endl;
        break;
        }
    }
    if (cou >0)
     cout<<"PRIME"<<endl;

    return 0;
}