#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout<<"Welcome to Rock, Paper and Scissors Game \n";
    char c; //Variable defined for storing player's choice
    cout<<"Enter any character to start\n";
    cin>>c;
    char choices[3]={'r','p','s'}; //Stores the choices available for the computer
    int player_score=0;// This stores the player score.
    int computer_score=0; // This stores the computer score.
    int player_temp=0 ,computer_temp=0;
    while(true) //Loop runs until this is true.
    {
        //The current score gets printed.
        cout<<"Player's score: "<<player_score<<"\n";
        cout<<"Computer's score: "<<computer_score<<"\n";
        //Comparing scores to determine the current winner.
        if(player_score==computer_score)
            cout<<"It's a Tie\n";
        else if(player_score>computer_score)
            cout<<"Player is winning\n";
        else
            cout<<"Computer is winning\n";
        cout<<"Press \nr for rock \np for paper \ns for scissors \nw to reset the game \nq to quite game \n";
        cin>>c; //Inputting the choice
        //This helps to clear the screen each time a move is made.
        for(int i=0;i<100;i++)
            cout<<"\n";
        char c1=choices[rand()%3]; //This makes the random choice.
        cout<<"Player's choice:\t"<<c<<"\n";
        cout<<"Computer's choice:\t"<<c1<<"\n";
        if(c==c1)
            continue;
        //Incrementing the score whenever the computer wins and vice versa.
        else if(c=='r')
        {
            if(c1=='p')
                computer_score++;
            else
                 player_score++;
        }
        else if(c=='p')
        {
            if(c1=='r')
                 player_score++;
            else
                 computer_score++;
        }
        else if(c=='s' )
        {
            if(c1=='p')
                 player_score++;  
            else
                 computer_score++;  
        }
        //This resets the scores.
        else if(c=='w')
        {
            player_score=0;
            computer_score=0;
            continue;
        }
        //This ends the loop.
        else if(c=='q')
        {
            cout<<"Game over\n";
            break;
        }
        // This handles invalid input.
        else
        {
            cout<<"Invalid option\n";
            break;
        }
    }
    return 0;
}