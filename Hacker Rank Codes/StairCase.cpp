#include <bits/stdc++.h>

using namespace std;

void staircase(int n) {
     int space=n-1;
     int hash=1;
  for(int j=0;j<n;j++){
    //space print
    for(int i=0;i<space;i++)
        cout<<" ";
    //hash print
    for(int i=0;i<hash;i++)
        cout<<"#";
    cout<<endl;
     space--;
     hash++;
  }
}

int main() {
    int n;
    cin >> n;
    staircase(n);
    return 0;
}

