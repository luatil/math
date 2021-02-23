#include <iostream>

int f(int x) {
    static int y = 0;
    y += x;
    return y;
}

int main()
{
    std::cout << f(1) << "\n";
    std::cout << f(1) << "\n";
    std::cout << f(1) << "\n";
    std::cout << f(1) << "\n";
    std::cout << f(1) << "\n";
}
