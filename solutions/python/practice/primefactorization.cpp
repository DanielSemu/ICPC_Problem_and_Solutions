
// #include<bits/stdc++.h>
// using namespace std;
// //PRIME FACTORS WITH BRUTE FORSE
// // void primefactor(int num){
// //   for(int i=2; i<=num; i++){
// //     if(num%i==0){
// //         int co=0;
// //         while(num%i==0){
// //             co++;
// //             num/=i;
// //         }
// //         cout<<i<<"^"<<co<<", ";-
// //     }

// //   }
// //   cout<<endl;
// // }
// ////Naive Sulution O(sqrt(n)) its best it works until 10^10
// void primefactor(int n){
//       while (n%2 == 0)
//       {
//         printf("%d ", 2);
//         n=n/2;
//       }
//       for(int i=3; i*i<=n; i=i+2 ){
//         while(n%i==0){
//            printf("%d ", i);
//           n/=i;
//         }
//       }
//       cout<<endl;
//       if(n>2){
//          printf ("%d ", n);
//       }
// }
// ////Seive prime factorization
// //first we find the smallest prime factor
// // #define MAXN 100001
// // int spf[MAXN];
// // // Calculating SPF (Smallest Prime Factor) for every number till MAXN.
// // void sieve(){
// // spf[1]=1;
// // for( int i=2; i<MAXN; i++)
// // spf[i]=i;
// // for(int i=4; i<MAXN; i+=2)
// // spf[i]=2;
// // for(int i=3; i*i<MAXN; i++){
// //   if(spf[i] == i){
// //     for(int j=i*i; j<MAXN; j++)
// //     if(spf[j]==j)
// //     spf[j]=i;
// //   }
// // }
// // }
// // vector<int> getFactorization(int x)
// // {
// //     vector<int> ret;
// //     while (x != 1)
// //     {
// //         ret.push_back(spf[x]);
// //         x = x / spf[x];
// //     }
// //     return ret;
// // }
// int main(){
//      //sieve();
//      int n;
//     while (1){
//     cin>>n;
//     if(n==-1)
//     break;
//    primefactor(n);
//     //  vector <int> p = getFactorization(n);
 
//     // for (int i=0; i<p.size(); i++)
//     //     cout << p[i] << " ";
//     //     cout << endl;
//     // 
//     }

//     return 0;
// }

/////////////////////PRIME FACTOR FOR MULTIPLE QUERIES  Time Complexity : O(nloglogn)

// C++ program to find prime factorization of a
// number n in O(Log n) time with precomputation
// allowed.
#include "bits/stdc++.h"
using namespace std;
 
#define MAXN   100001
int spf[MAXN];
void sieve()
{
    spf[1] = 1;
    for (int i=2; i<MAXN; i++)
        spf[i] = i;
    for (int i=4; i<MAXN; i+=2)
        spf[i] = 2;
 
    for (int i=3; i*i<MAXN; i++)
    {
        if (spf[i] == i)
        {
            for (int j=i*i; j<MAXN; j+=i)
                if (spf[j]==j)
                    spf[j] = i;
        }
    }
}
vector<int> getFactorization(int x)
{
    vector<int> ret;
    while (x != 1)
    {
        ret.push_back(spf[x]);
        x = x / spf[x];
    }
    return ret;
}
int main(int argc, char const *argv[])
{
    sieve();
    int x = 12246;
    cout << "prime factorization for " << x << " : ";
    vector <int> p = getFactorization(x);
    for (int i=0; i<p.size(); i++)
        cout << p[i] << " ";
    cout << endl;
    return 0;
}
