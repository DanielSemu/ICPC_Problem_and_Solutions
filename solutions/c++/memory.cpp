#include <bits/stdc++.h>
using namespace std;
int main(){
map <string,int> m;
m.insert(pair<string,int>("bool", 1));
m.insert(pair<string,int>("char", 1));
m.insert(pair<string,int>("int", 4));
m.insert(pair<string,int>("double", 8));
m.insert(pair<string,int>("float", 4));
int x, sum =0;
cin>>x;
string na[x];
int no[x];
for (int i=0; i<x; i++){
	cin>>na[i]>>no[i];
}

for (int i=0; i<x; i++){
	sum = sum + (m[na[i]]*no[i]);
}
cout<<sum<<endl;
}
