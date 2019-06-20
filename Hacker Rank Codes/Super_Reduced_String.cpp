#include<iostream>
#include <string>
using namespace std;
string super_reduced_string(string s)
{
	int len = s.length();
	for (int i = 0; i<len - 1; ++i)
	{
		if (s.at(i) == s.at(i + 1))
		{
			s.erase(i, 2);//erase similar 2 characters from ith position...
			i = -1;
		}
		len = s.length();
	}
	if (s.length() == 0)
		return "Empty String";
	else return s;
}
int main()
{
	string s;
	cin >> s;
	string result = super_reduced_string(s);
	cout << result << endl;
	//system("pause");
	return 0;
}
