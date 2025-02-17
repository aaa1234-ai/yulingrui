#include <iostream>
using namespace std;
const int INCH_PER_FEET = 12;         //1英尺为12英寸;
const double POUND_PER_KG = 2.2;      //1千克为2.2磅;
const double METER_PER_INCH = 0.0254; //1英寸为0.0254米;

int main()
{
    double height_feet, height_inch, weight, meter;

    cout << "Please enter your height in feet and inch: ";
    cin >> height_feet >> height_inch;
    cout << "Please enter your weight in pound: ";
    cin >> weight;

    cout << "Your height is " << height_feet * INCH_PER_FEET + height_inch << " inches." << endl;
    meter = (height_feet * INCH_PER_FEET + height_inch) * METER_PER_INCH;
    cout << "Your BMI is " << (weight / POUND_PER_KG) / (meter * meter) << "." << endl;

    return 0;
}
