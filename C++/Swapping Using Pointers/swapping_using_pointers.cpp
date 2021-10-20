
//SWAPING USING POINTER

#include<iostream>
using namespace std;
void swap(int *a, int *b){
  int temp = *a ;
  *a = *b;
  *b = temp;
  
}
int main(){
int a =4;
int b = 6;
int *aptr = &a;
int *bptr = &b;
swap(aptr ,bptr);
cout<<a<<" "<<b<<end;
 }
