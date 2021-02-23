#include <stdio.h> 

int main()
{
	int a = 10;
	char *b = &a;
	printf("%p %p\n", &a, &b);
	*(b+1) = 1;
	printf("%d", a);
}
