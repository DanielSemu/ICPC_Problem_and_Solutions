#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

ll findlcm(vector<int>arr, int n)
{
    ll ans = arr[0];
    for (int i = 1; i < n; i++)
        ans = (((arr[i] * ans)) /
                (gcd(arr[i], ans)));
 
    return ans;
}

int main()
{ 
  int x;
  vector<int>arr;
    while(1){
        while(1){
            cin>>x;
            
            arr.push_back(x);
        }
        if (sizeof(arr)==0)
        break;
    
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("%lld", findlcm(arr, n));
    }
    return 0;
}