#include <bits/stdc++.h>
using namespace std;
// Defining global variables 
const int Max_size=1e3+1;
int first_matrix_row=0;
int first_matrix_column=0;
int second_matrix_row=0;
int second_matrix_column=0;
// Function performing matrix multiplication
void multiply(int first_matrix[Max_size][Max_size], int second_matrix[Max_size][Max_size])
{
  int mul[first_matrix_row][second_matrix_column];
   for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<second_matrix_column;j++)
                    mul[i][j]=0;
            }
        if(first_matrix_column==second_matrix_row)// Checking the validation of multiplication 
        {
            for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<second_matrix_column;j++)
                {
                   for(int k=0;k<first_matrix_column;k++)
                        mul[i][j]+=(first_matrix[i][k]*second_matrix[k][j]);                   
                }
            }
             // displaying the multiplied matrix 
            for(int i=0;i<first_matrix_row;i++)
                {
                    for(int j=0;j<second_matrix_column;j++)
                        cout<<mul[i][j]<<" ";
                    cout<<"\n";
                }
        }
        else
            cout<<"Invalid dimensions\n";
}
// Function performing matrix addition
void add(int first_matrix[Max_size][Max_size], int second_matrix[Max_size][Max_size])
{
     if(first_matrix_row==second_matrix_row && first_matrix_column==second_matrix_column)// Checking the validation of addition 
        {
            int add[first_matrix_row][first_matrix_column];
            for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<first_matrix_column;j++)
                    add[i][j]=first_matrix[i][j]+second_matrix[i][j];
            }
            // Displaying the added matrix
             for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<first_matrix_column;j++)
                    cout<<add[i][j]<<" ";
                cout<<"\n";
            }
        }
        else
            cout<<"Invalid operation\n";
}
// Function performing the matrix subtraction
void subt(int first_matrix[Max_size][Max_size], int second_matrix[Max_size][Max_size])
{
     if(first_matrix_row==second_matrix_row && first_matrix_column==second_matrix_column)// Checking the validation for subtraction
        {
            int subt[first_matrix_row][first_matrix_column];
            for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<first_matrix_column;j++)
                    subt[i][j]=first_matrix[i][j]-second_matrix[i][j];
            }
            //displaying the subtracted matrix
             for(int i=0;i<first_matrix_row;i++)
            {
                for(int j=0;j<first_matrix_column;j++)
                    cout<<subt[i][j]<<" ";
                cout<<"\n";
            }
        }
        else
            cout<<"Invalid operation\n";
}
int main()
{
    //Enter your choice 
    cout<<"Enter the operation to be performed \n1 for Matrix Multiplication\n2 for Matrix Addition \n3 for Matrix Subtraction \n4 for Finding Inverse \n";
    int n;
    cin>>n;
    // User'entry for the size of first matrix
    cout<<"Enter the size for the first matrix:\n";
    cin>>first_matrix_row;
    cin>>first_matrix_column;
    cout<<"Enter the first matrix:\n"; // Input of first matrix
    int first_matrix[Max_size][Max_size];
    for(int i=0;i<first_matrix_row;i++)
    {
        for(int j=0;j<first_matrix_column;j++)
            cin>>first_matrix[i][j];
    }
    // User'entry for the size of second matrix
    cout<<"Enter the size for the second matrix:\n";
    cin>>second_matrix_row;
    cin>>second_matrix_column;
    cout<<"Enter the second matrix:\n"; // Input of second matrix
    int second_matrix[Max_size][Max_size];
    for(int i=0;i<second_matrix_row;i++)
    {
        for(int j=0;j<second_matrix_column;j++)
            cin>>second_matrix[i][j];
    }
    // Operations to be followed as per user's choice
    if(n==1)
    {
       multiply(first_matrix,second_matrix);
    }
    else if(n==2)
    {
       add(first_matrix,second_matrix);
    }
    else if(n==3)
    {
     subt(first_matrix,second_matrix);  
    }
    return 0;

}