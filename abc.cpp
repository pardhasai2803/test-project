#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(int a, int b) {
    if (b == 0) {
        throw runtime_error("Division by zero");
    }
    return (double)a / b;
}

int main() {
    int x = 10;
    int y = 5;

    cout << "Add: " << add(x, y) << endl;
    cout << "Subtract: " << subtract(x, y) << endl;
    cout << "Multiply: " << multiply(x, y) << endl;
    cout << "Divide: " << divide(x, y) << endl;

    return 0;
}
