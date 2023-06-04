
import math
z,x,y=map(int, input().split())
ss=(x*x)+(y*y)
len=math.sqrt(ss)
for i in range(z):
    z=int(input())
    if (z <= len):
        print("DA")
    else:
        print("NE")



# Submission 9142759
# Edit and resubmit
# ID	DATE	PROBLEM	STATUS	CPU	LANG	TEST CASES
# 9142759	21:11:23	Sibice	
# Accepted
# 0.00 s	C++	
# 12/12
# Files submitted
# sibice.cpp
# Download file
# #include <iostream>
# #include <cmath>

# using namespace std;

# int main() {
#     int n;
#     cin >> n;

#     double x, y;
#     cin >> x >> y;

#     double length = sqrt((x*x)+(y*y));

#     for(int i = 0; i < n; i++) {
#         int temp;
#         cin >> temp;
#         if(temp <= length) {
#             cout << "DA" << endl;
#         }
#         else {
#             cout << "NE" << endl;
#         }
#     }
# }