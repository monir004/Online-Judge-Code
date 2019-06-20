#include <iostream>
#include<string>
#include<sstream>

using namespace std;
//Nice C code...
/*int main() {
    int hh, mm, ss ;
    char t12[3];
    scanf("%d:%d:%d%s", &hh, &mm, &ss, t12) ;

    if (strcmp(t12,"PM")==0 && hh!=12) hh += 12 ;
    if (strcmp(t12,"AM")==0 && hh==12) hh = 0 ;

    printf("%02d:%02d:%02d", hh, mm, ss) ;
    return 0;
}*/
string timeConversion(string s) {
	if (s.compare(8,2,"AM")==0) //8th and 9th position string AM checks with AM.
	{
		if (s.compare("12:00:00:AM")==0)
			return "00:00:00";
		else if(s.compare(0,2,"12")==0){
			string res= s.replace(0, 2, "00");
			return res.erase(8, 2);
		}
		else return s.erase(8, 2);
	}
	else {
		if (s.compare(0, 2, "12") == 0)
		{
			return s.erase(8, 2);
		}
		else {
			string s2 = s.substr(0, 2);//finding the hours of PM
			s.erase(0, 2);//removing first two characters of the string as it will be used for calculation
			//converting string to int here
			stringstream ss(s2); //can write istringstream
			int value;
			ss >> value;

			//have to  learn sstream in great details...



			value += 12;
			stringstream sss; //can write ostringstream,output strin stream
			sss << value;
			string res = sss.str();

			return (res + s).erase(8, 2);
			cout << value << endl;
		}

	}
}

int main() {
	string s;
	while (cin >> s) {
		string result = timeConversion(s);
		cout << result << endl;
	}
	return 0;
}

