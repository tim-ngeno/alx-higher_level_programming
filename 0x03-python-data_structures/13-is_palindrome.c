#include "lists.h"

/**
 * check_palindrome - checks palindrome
 * @first: points to nodes from start
 * @last: points to nodes from end
 * Return: 1 if is a palindrome, 0 otherwise
 */
int check_palindrome(listint_t **first, listint_t *last)
{
	int a;

	if (last == NULL)
		return (1);
	a = check_palindrome(first, last->next);

	if (a == 0)
		return (0);

	if ((*first)->n == last->n)
		a = 1;
	else
		a = 0;

	*first = (*first)->next;
	return (a);
}


/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to pointer of head node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t **temp, *current;

	temp = head;
	current = *head;

	if (*head == NULL)
		return (1);

	return (check_palindrome(temp, current));
}
