#include <iostream>
#include <stdexcept>

using namespace std;

int add(int a, int b) {
    // Time complexity: O(1)
    // Space complexity: O(1)
    return a + b;
}

int subtract(int a, int b) {
    // Time complexity: O(1)
    // Space complexity: O(1)
    return a - b;
}

int multiply(int a, int b) {
    // Time complexity: O(1)
    // Space complexity: O(1)
    return a * b;
}

double divide(int a, int b) {
    // Time complexity: O(1)
    // Space complexity: O(1)
    if (b == 0) {
        throw logic_error("Division by zero");
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