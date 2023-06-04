#include<bits/stdc++.h>
using namespace std;
#define N 100000
vector<int> gr1[N] , gr2[N];
bool vis1[N] , vis2[N];
void Add_edge(int u , int v){
    gr1[u].push_back(v);
    gr2[v].push_back(u);

}
void dfs1(int x){
    vis1[x]= true;
    for (auto i : gr1[x])
        if( !vis1[i])
        dfs1(i);
}
void dfs2(int x){
    vis2[x]=true;
    for ( auto i : gr2[x])
    if (!vis2[x])
    dfs2(i);
}
bool is_connected(int n){

    memset(vis1, false, sizeof vis1);
    dfs1(1);
    memset( vis2, false, sizeof vis2);
    dfs2(1);
    for ( int i=1;i<=n; i++ ){
        if ( !vis1[i] and !vis2[i])
        return false;
    }
    return true;
}
int main(){

int n,m,a,b;
cin>>n>>m;
for ( int i=0; i<m; i++){
cin>>a>>b;
Add_edge(a,b);
}
if (is_connected(m))
    cout<<"YES"<<endl;
else
    cout<<"NO"<<endl;
    return 0;
}