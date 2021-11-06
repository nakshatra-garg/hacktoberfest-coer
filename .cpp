#include <cstdlib>
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
float sine,cosine,tangent,cotangent,cosecant,secant;
float rad,degree;
rad = degree = 0.0;
int choice;

//sine=cosine=tangent=cotangent=cosecant=secant = 0.0;

cout <<"1. Find trig ratios using radian measure:" << endl;
cout <<"2. Find trig ratios using length of sides:" << endl;

cout <<"Enter your choice:";
cin >> choice;

if(choice == 1)
{



cout << "Enter the angle in degrees:";
cin >> degree;

rad = (degree/180) * 3.14;

sine = sin(rad);
cosine = cos(rad);
tangent = tan(rad);
secant = 1/cosine;
cosecant = 1/sine;
cotangent = cosine/sine;



}
else if(choice == 2)
{
float opposite,adjacent,hypotenuse;

cout << "Enter the length of each side:" << endl; 
cout << "Length of opposite side(AB)?:" << endl;
cin >> opposite;

cout << "Length of adjacent side(BC)?:" << endl;
cin >> adjacent;

cout << "Length of hypotenuse (AC)?:" << endl;
cin >> hypotenuse;

sine = opposite/hypotenuse;
cosine = adjacent/hypotenuse;
tangent = opposite/adjacent;
secant = 1/cosine;
cosecant = 1/sine;
cotangent = cosine/sine;


}
else
{

cout << "Incorrect ! Choose correct option:" << endl;

} 

//checking valid values for sin,cos,tan,cosec,sec,cot before printing



if(sine >= -1.0 || sine <= 1.0)
{

cout << "Sin" << " " << degree << "=" << sine << endl;
} 
else
{
cout << "Sin" << "=" << "Undefined" << endl;
}

if(cosine >= -1.0 || cosine <= 1.0)
{

cout << "Cos" << " " << degree << "=" << cosine << endl;
}
else 
{
cout << "Cos" << "=" << "Undefined" << endl;
}



if(degree != 90)
{ 
cout << "Tan" << " " << degree << "=" << tangent << endl;
} 
else
{

cout << "Tan" << "=" << "Undefined" << endl;
} 

if(degree != 90)
{
cout << "Sec" << " " << degree << "=" << secant << endl;
} 
else
{
cout << "Sec" << "=" << "Undefined" << endl;

} 

if(degree != 0 && cosecant <= -1.0 || cosecant >= 1.0)
{
cout << "Cosecant" << " " << degree << "=" << cosecant << endl; 
}
else
{

cout << "Cosecant" << "=" << "Undefined" << endl;
}

if(degree != 0)
{
cout << "Cotangent" << " "<< degree << "=" << cotangent << endl;
}
else
{
cout << "Cotangent" << " " << "=" << "Undefined" << endl;
}

system("PAUSE");

return EXIT_SUCCESS;
}
