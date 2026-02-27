#include<iostream>
using namespace std;

void solve(string s)
{
    int size = s.length();
    int j = size/2;

    if (size % 2 != 0) { // Symmetry makes sense for even-length strings
        cout << "Not symmetrical" << endl;
        return;
    }

    for(int i = 0 ; i < size/2 ; i++,j++)
    {
        if(s[i] != s[j] )
        {
            cout<<"Not symmetrical"<<endl;
            return;
        }
    }
    cout<<"SYm" <<endl;
}
int main()
{
    string s ;
    cout<<"enter string "<<endl;
    cin>>s;

    solve(s);
}