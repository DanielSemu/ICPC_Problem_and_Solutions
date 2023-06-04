#include <iostream>
using namespace std;

int main(){
    int a,b,c,d;
    double g=0,e=0;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;

    g = (a+b)/2. + (c+d)/2.;

    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;

    e = (a+b)/2. + (c+d)/2.;
    
    if (g>e)
        cout << "Gunnar" << endl;
    else if (e>g)
        cout << "Emma" << endl;
    else
        cout << "Tie" << endl;
    return 0;
}
