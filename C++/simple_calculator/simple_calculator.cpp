#include <bits/stdc++.h>
//includeing the libraries
#define int long double
//To deal with larger numbers
using namespace std;
int32_t main() //int is replaced by long double, but main has to be int type.
{
    cout<<"Welcome to my Calculator.\n";
    int a=0,x;
    //These are the variables storing the operands
    cout<<"Press +,-,*,/ or % to perform the corresponding operation.\n";
    cout<<"Enter q to quit the calculator and r to reset value to 0.\n";
    char ch;
    //It is used to store the operator
    cout<<"Enter first operand:\t";
    cin>>a;
    while(ch!='q')
    // This runs the program until q is supplied as an operand
    {
        cout<<"Current Value:\t"<<a<<"\n";
        //This keeps printing the value after each operation.
        cout<<"Enter operator:\t";
        cin>>ch;
        //Inputting the operator
        if(ch=='q')
            break;
        //This is to quit from the calculator
        else if(ch=='r')
        {
            //This is used to reset the value to 0
            a=0;
            continue;
        }
        cout<<"Enter operand:\t";
        cin>>x;
        //This inputs the operand.
        switch(ch)
        {
            //Now, this is for performing the various operations.
            case '+': a+=x;break;
            case '-': a-=x;break;
            case '*': a*=x;break;
            case '/': a/=x;break;
            case '%': a=(long long)a%(long long)x;break;
            //Modulus needs the operands to be of integer type
            default: cout<<"Invalid operand\n";
            //In case an invalid character is given.
        }
    }
    return 0;
}