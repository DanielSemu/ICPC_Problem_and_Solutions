#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
   string s;
   cin>>x;
   for(int i=0;i<x;i++){
       cin>>s;
       int n=s.size();
      
while (s.substr(0,n/2)!=s.substr(n/2,n/2)){
    n--;
}
      string y=s.substr(0,n/2);
      string ss=y; 
      while(y.size()<s.size()){
        y.append(y);
      }
      y.erase((y.find(ss)),ss.size());
y.erase(0,s.size());
        while(y.size()<8){
        y.append(ss);
     }
     y.erase(8,y.size()-1);
     cout<<y<<"..."<<endl;
     
   }
    return 0;
}
// #include<bits/stdc++.h>
// using namespace std;
// int main()
// {
//     char str[2001],str1[1000],str2[1000];
//     int i,j,k,len,x,m,t,p,y,check,w,n;
//     scanf("%d",&t);
//     getchar();
//     while(t--){
//     cin>>str;
//     len=strlen(str);
//     x=len/2;
//     do{
//     m=0,n=0;
//     for(i=0;i<x;i++){
//         str1[m++]=str[i];
//         str2[n++]=str[i+x];
//     }
//         str1[m]=str2[n]='\0';

//     x--;
//     }   while(strcmp(str1,str2)!=0);
//     y=strlen(str1);
//     w=len-2*y;
//     check=0;
//     while(check!=9){
//     for(i=0+w;i<y;i++){
//             check++;
//             if(check==9) break;
//         printf("%c",str1[i]);
//     }
//     w=0;
//     }
//     printf("...\n");
//     }
// }