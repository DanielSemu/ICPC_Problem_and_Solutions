
#include <bits/stdc++.h>
typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
using namespace std;
int main(){
    while(true){
                int N;
                cin>>N;
                if(N == 0)
                        break;
                while(N--){

                           int A, B, C, D, E;

                           cin>>A>>B>>C>>D>>E;

                           if(A<=127 && B>127 && C>127 && D>127 && E>127)

                                     cout<<"A\n";

                           else if(A>127 && B<=127 && C>127 && D>127 && E>127)

                                cout<<"B\n";

                           else if(A>127 && B>127 && C<=127 && D>127 && E>127)

                                cout<<"C\n";

                           else if(A>127 && B>127 && C>127 && D<=127 && E>127)

                                cout<<"D\n";

                           else if(A>127 && B>127 && C>127 && D>127 && E<=127)

                                cout<<"E\n";

                           else

                               cout<<"*\n";

                }

    }

    return 0;

}
