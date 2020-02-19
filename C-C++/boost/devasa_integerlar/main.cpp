// Bu program boost kutuphanesini kullanarak cok buyuk tam sayi degerleri ile
// islem yapmamiza imkan sagliyor.

// int128_t buyuk tam sayiyilari ifade ediyor.


#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;
using namespace std;


void boost_product(long long A, long long B, int op)
{
    switch(op)
    {
        case 1:
            cout << "Product of "<< A <<" + "<< B <<" = "<<((int128_t) A + B);
            break;
        case 2:
            cout << "Product of "<< A <<" - "<< B <<" = "<<((int128_t) A - B);
            break;
        case 3:
            cout << "Product of "<< A <<" * "<< B <<" = "<<((int128_t) A * B);
            break;
        case 4:
            cout << "Product of "<< A <<" / "<< B <<" = "<<((int128_t) A / B);
            break;
        default:
            cout << "Undefined value!";
            break;
    }
}


int main()
{
    long long first,second;
    int op;
    cout << "Enter the number 1: ";
    cin >> first;
    cout << "Enter the number 2: ";
    cin >> second;
    cout << "\n 1)[#] + \n 2)[#] - \n 3)[#] * \n 4)[#] / \n\n [^-^] Select an operand number: ";
    cin >> op;
    boost_product(first,second,op);
}
