WAP to take a string as a Input. Program will determine whether each left parenthesis has a matching with right parenthesis.

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int flag = 0;
    string input;
    stack<char> s;

    getline(cin, input);

    for(auto &x:input)
    {
        if(x == '(')
            s.push(x);

        else if(x == ')')
        {
            if(s.empty())
            {
                flag = 1;
                break;
            }
            
            else
                s.pop();
        }
    }

    if(!s.empty())
        flag = 1;

    cout<<flag<<'\n';
    

    return 0;
}
