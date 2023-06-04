#include <bits/stdc++.h>
using namespace std;
int hexadecimalToDecimal(string hexVal)
{
    int len = hexVal.size();
    int base = 1;
    int dec_val = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (hexVal[i] >= '0' && hexVal[i] <= '9') {
            dec_val += (int(hexVal[i]) - 48) * base;
            base = base * 16;
        }
        else if (hexVal[i] >= 'A' && hexVal[i] <= 'F') {
            dec_val += (int(hexVal[i]) - 55) * base;
            base = base * 16;
        }
    }
    return dec_val;
}
int octalToDecimal(int n)
{
    int num = n;
    int dec_value = 0;
    int base = 1;
    int temp = num;
    while (temp) {
        int last_digit = temp % 10;
        temp = temp / 10;
        dec_value += last_digit * base;
        base = base * 8;
    }
    return dec_value;
}
int main(){
	while (1) {
	 int x,y,out;
	 string op,xx;
	 cin>>xx>>y;
	 if (xx== "0" && y==0 )
	 break;
	 if(xx.at(0)== '0' && xx.at(1)!='X'){
	 	stringstream geek(xx);
        x = 0;
        geek >> x;
	 	x=octalToDecimal(x);
	 }
	 else if(xx.at(0)=='0' && xx.at(1)=='X'){
	 	x=hexadecimalToDecimal(xx);
	 
	 }
	 else{
	 	stringstream geek(xx);
        x = 0;
       geek >> x;
	 }
	 int rank=0;
	 for (int i=0; i<y; i++){
	 	cin>>op>>out;
	 	if(op == "++i"){
	 		if (++x == out){
	 			rank+=1;
			 }
			 else{
			 	x=out;
			 }
		 }
		 else if(op == "i++"){
		 	
	 		if (x++ == out){
	 			rank+=1;
			 }
			 else{
			 	x=out;
			 }
		 }
		 else if(op == "i--"){
		 	
	 		if (x-- == out){
	 			rank+=1;
			 }
			 else{
			 	x=out;
			 }
		 }
		 else if(op == "--i"){
		 	
	 		if (--x == out){
	 			
	 			rank+=1;
			 }
			 else{
			 	x=out;
			 }
			  
		 }
		else if(op == "i"){
	 		if (x == out){
	 			rank+=1;
			 }
			  else{
			 	x=out;
			 }
		 }
	 }
	cout<<rank<<endl;
	}
}
