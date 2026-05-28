/**
 * @file abc.cpp
 * @brief Basic arithmetic operations on integers.
 * 
 * This file provides functions for addition, subtraction, multiplication, and division.
 * The division operation throws a logic_error if the divisor is zero.
 * 
 * Time complexities and space complexities for each function are documented in-line.
 */

#include <iostream>
#include <stdexcept>

using namespace std;

/**
 * @brief Adds two integers.
 * 
 * @param a The first integer.
 * @param b The second integer.
 * 
 * @return The sum of a and b.
 * 
 * Time complexity: O(1)
 * Space complexity: O(1)
 */
int add(int a, int b) {
    return a + b;
}

/**
 * @brief Subtracts one integer from another.
 * 
 * @param a The first integer.
 * @param b The second integer.
 * 
 * @return The difference of a and b.
 * 
 * Time complexity: O(1)
 * Space complexity: O(1)
 */
int subtract(int a, int b) {
    return a - b;
}

/**
 * @brief Multiplies two integers.
 * 
 * @param a The first integer.
 * @param b The second integer.
 * 
 * @return The product of a and b.
 * 
 * Time complexity: O(1)
 * Space complexity: O(1)
 */
int multiply(int a, int b) {
    return a * b;
}

/**
 * @brief Divides one integer by another.
 * 
 * @param a The dividend.
 * @param b The divisor.
 * 
 * @return The quotient of a and b.
 * 
 * @throws logic_error if b is zero.
 * 
 * Time complexity: O(1)
 * Space complexity: O(1)
 */
double divide(int a, int b) {
    if (b == 0) {
        throw logic_error("Division by zero");
    }
    return (double)a / b;
}

/**
 * @brief Main program entry point.
 */
int main() {
    int x = 10;
    int y = 5;

    cout << "Add: " << add(x, y) << endl;
    cout << "Subtract: " << subtract(x, y) << endl;
    cout << "Multiply: " << multiply(x, y) << endl;
    try {
        cout << "Divide: " << divide(x, y) << endl;
    } catch (const logic_error& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}