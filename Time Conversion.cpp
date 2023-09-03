#include <bits/stdc++.h>
#include<iostream>
#include <string>
using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string add_leading_zeros(const string& str, int width) {
  stringstream ss;
  ss << setw(width) << setfill('0') << str;
  return ss.str();
}

string timeConversion(string s) {
    
    auto hh = stoi(s.substr(0,2));
    auto ampm = s.substr(8,2);
    
    hh= hh % 12;        
    if (ampm == "PM") hh += 12;
    
    return add_leading_zeros(to_string(hh),2) + s.substr(2,6);

}



int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
