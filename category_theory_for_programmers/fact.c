#include <stdio.h>

int factorial(int n)
{	
	int result = 1;
	for(int i = 2; i <= n; i++)
		result *= i;
	return result;
}

int main()
{
	printf("%d", factorial(10));
}
