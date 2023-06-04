#include <iostream>
#include <cctype>
#include <cstdio>
#include <vector>
using namespace std;
int  caso = 1;
void printHeader()
{
    printf("Case %d:\n", caso++);
    printf("#include<string.h>\n");
    printf("#include<stdio.h>\n");
    printf("int main()\n");
    printf("{\n");
}

void printInput(string str)
{   
    printf("printf(\"");
    for(int c=0; c<str.size(); c++)
    {
        if(isalnum(str[c]) || isspace(str[c]))
          printf("%c",str[c]);
        else if(str[c] == '\"')
                printf("\\\"");
        else if(str[c] == '\'')
                printf("\\\'");
        else if(str[c] == '\\')
                printf("\\\\");
    }
    printf("\\n\");\n");
}

void printFooter()
{
    printf("printf(\"\\n\");\n");
    printf("return 0;\n");
    printf("}\n");
}

int main()
{
int lines;
string str;

while(scanf("%d", &lines))
{
    if(!lines)
       break;

    vector<string> vec;
    getline(cin,str);
    for(int a=0; a<lines; a++)
    {
        getline(cin, str);
        vec.push_back(str);
    }
    printHeader();    
    for(int x=0; x<vec.size(); x++)
        printInput(vec[x]);
    printFooter();
}
return 0;
}




