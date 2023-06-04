#include <bits/stdc++.h>
using namespace std;
int main(){
int t;
cin>>t;
string name[t];
int yr[t],month[t],day[t];
int maxy=0, maxm=0, maxd=0, miny= 10000,minm= 12,mind= 31, index = 0;
for (int i=0; i<t; i++){
	cin>>name[i]>>day[i]>>month[i]>>yr[i];
}
for (int i=0; i<t; i++){
	if(yr[i]>maxy){
		maxy = yr[i];
		maxm = month[i];
		maxd = day[i];
		index = i;
	}
	else if(yr[i]== maxy){
		if(month[i]>maxm){
				maxy = yr[i];
		maxm = month[i];
		maxd = day[i] ;
			index = i;
		}
		else if(month[i]== maxm){
			if(day[i]>maxd){
					maxy = yr[i];
		maxm = month[i];
		maxd = day[i];
				index = i;
			}
			else if(day[i]== mind){
				
			}
		}
	}
}
cout<<name[index]<<endl;
for (int i=0; i<t; i++){
	if(yr[i]<miny){
		miny = yr[i];
		minm = month[i];
		mind = day[i];
		index = i;
	}
	else if(yr[i]== miny){
		if(month[i]<minm){
			miny = yr[i];
		minm = month[i];
		mind = day[i];
			index = i;
		}
		else if(month[i]== minm){
			if(day[i]<mind){
				miny = yr[i];
		minm = month[i];
		mind = day[i];
				index = i;
			}
			else if(day[i]== mind){
				
			}
		}
	}
}
cout<<name[index]<<endl;




return 0;
}
