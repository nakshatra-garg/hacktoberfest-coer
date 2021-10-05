#include<iostream>
using namespace std;

int main(){

char op;         // op denotes operator vaiable.
int num1, num2;

cout <<"Enter the value of operator ( +,-,*,/,% ) :";
cin>>op;

cout<<"Enter num1 :"<<endl;
cin>>num1;
cout<<"Enter num2 :"<<endl;
cin>>num2;

switch(op){

case '+':
cout<<num1<<"+"<<num2<<"="<<(num1+num2);
break;

case '-':
cout<<num1<<"-"<<num2<<"="<<(num1-num2);
break;

case '*':
cout<<num1<<"*"<<num2<<"="<<(num1*num2);
break;

case '/':
if(num2 != 0.0 )
cout<<num1<<"/"<<num2<<"="<<(num1/num2);
else
cout<<"Divide by zero situation";
break;

case '%':
if (num2 != 0.0 )
cout<<num1<<"%"<<num2<<"="<<(num1 % num2);
else
cout<<"Modulus by zero situation";

break;

default:                              // Using default for invalid operaors in a program like ^.
cout<< op <<"Invalid operator";

}

return 0;

}

























