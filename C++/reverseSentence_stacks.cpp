/*
Problem Description

Given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

*/

string Solution::solve(string A) {
    stack<string> st;
    string temp="",ans="";
    
    if(A.size()==1) return A; 
  
    for(int i=0;i<A.size();i++){
        if(A[i]==' '){          // check for space between strings and push the temp string to stack
            if(temp.size())
            st.push(temp);
            temp="";
        }
        else {
            temp+=A[i];         // concat the character to temp if its not a space
        }
    }
  
    if(temp.size())
    st.push(temp);
    
    while(!st.empty()){
        ans+=st.top();
        st.pop();
        if(!st.empty()) ans+=" ";   //pop out the strings until stack is empty and concat them to ans
    }
    return ans;
}
