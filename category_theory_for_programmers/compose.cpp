#include <functional>
#include <iostream>
using namespace std;


auto compose = [] (auto f, auto g) {
	return [=](auto x) {
		return f(g(x));
	};
};

// does not work 
auto derivative = [](auto f){
	return [=](auto x) {
		return ((f(x+0.1) - f(x))/ 0.1);
	};
};

auto x_square(int x) -> int
{
	return x*4;
}

auto add2(int x) -> int
{
	return x+2;
}

int main()
{
	auto x_square_prime = derivative(x_square);
	cout << x_square_prime(100) << '\n';
}
