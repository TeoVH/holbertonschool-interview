#include "palindrome.h"

/**
 * is_palindrome - function that checks if given integer is a palindrome
 * @n: Number to be checked
 * Return: 1 if n is palindrome, 0 otherwise
 */

int is_palindrome(unsigned long n)
{
	unsigned long reversed = 0;
	unsigned long num = n;

	while (num != 0)
	{
		reversed = reversed * 10;
		reversed = reversed + num % 10;
		num = num / 10;
	}

	if (reversed == n)
		return (1);

	return (0);
}
