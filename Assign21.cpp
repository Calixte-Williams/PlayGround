
#include <iostream>
#include <string>
#include <iomanip>
#include "test.h"

using namespace std;
int main()
{
    double cost, discountAmount;
    int discountPercentage = 10;
    string output;

    cout << "Enter the cost of the item: \n";
    cin >> cost;

    do 
    {
        cout << discountPercentage << "\n";
        discountPercentage = discountPercentage + 5;
        //discountAmount = (discountPercentage / static_cast<double>(100)) * cost;
      //discountAmount = cost * discountPercentage;
        

      //output = "Discount amounts are: \n $ " << discountAmount << endl;
      //cout << "Discount Percentage: " << discountPercentage << endl;
      //output = "Discount amounts are: $ ";
      //cout << output << discountAmount;

        //discountPercentage = discountPercentage + 5;

        //while (discountPercentage == 40) {
          //  break; //End loop
        //}
            
        
    } while (discountPercentage < 40);
    //cout << "Discount Percentage: " << discountPercentage << endl;
    //cout << endl;
  

    



 

    

    return 0;
}