#include <iostream>
#include <string>
using namespace std;

int main()
{
    const int ArSize = 12;
    const string months[ArSize] = 
    {
        "January", "February","March", 
        "April", "May", "June", "July",
        "August","September", "October",
        "November", "December"
    };
    int sum, sales_volume[ArSize];

    for (int i = 0; i < ArSize; i++)
    {
        cout << "Please enter number of books sold (";
        cout << months[i] << "): ";
        cin >> sales_volume[i];
    }
    for (int i = 0; i < ArSize; i++)
    {
        sum += sales_volume[i];
    }
    cout << "A total of " << sum << " <<C++ For Fools>> books were sold in a year." << endl;

    return 0;
}
