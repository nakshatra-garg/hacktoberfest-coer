/*
Problem Description

Given a string A of size N.

Return the string A after reversing the string word by word using stacks.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

*/

string solve(string A) {
    stack<string> st;
    string temp="",ans="";
    
    if(A.size()==1) return A;
    for(int i=0;i<A.size();i++){
        if(A[i]==' '){             // check for space and push the string in temp to stack
            if(temp.size())
            st.push(temp);
            temp="";
        }
        else {
            temp+=A[i];             // if character is other than space then concat it into temp
        }
    }
    if(temp.size())
    st.push(temp);
    
    while(!st.empty()){
        ans+=st.top();
        st.pop();
        if(!st.empty()) ans+=" ";       // concat the string to ans until stack is empty
    }
    return ans;
}
