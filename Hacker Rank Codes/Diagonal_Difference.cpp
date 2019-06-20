#include <bits/stdc++.h>

using namespace std;

int diagonalDifference(vector < vector<int> > a) {
    // Complete this function
    //std::vector<std::vector<int>> matrix;
    //matrix.resize(no_of_rows, std::vector<int>(no_of_cols, initial_value));
    int n=a.size();
    int primary_diagonal=0,secondary_diagonal=0;
    for(int i=0;i<n;i++)
    {
        primary_diagonal+=a[i][i];
    }
    for(int i=0,j=n-1;i<n;i++,j--)
    {
        secondary_diagonal+=a[i][j];
    }
    return primary_diagonal>secondary_diagonal?primary_diagonal-secondary_diagonal:secondary_diagonal-primary_diagonal;
}

int main() {
    int n;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    int result = diagonalDifference(a);
    cout << result << endl;
    return 0;
}

