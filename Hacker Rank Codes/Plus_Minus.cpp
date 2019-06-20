#include <bits/stdc++.h>

using namespace std;

void plusMinus(vector <int> arr) {
    int positive=0,negative=0,zeroes=0;
    int n=arr.size();
    for(int i=0;i<n;i++)
    {
        if(arr[i]>0)
            positive++;
        else if (arr[i]<0)
            negative++;
        else zeroes++;
    }
    cout<<fixed<<setprecision(6)<<(double)positive/n<<endl;
    cout<<fixed<<setprecision(6)<<(double)negative/n<<endl;
    cout<<fixed<<setprecision(6)<<(double)zeroes/n<<endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    plusMinus(arr);
    return 0;
}

