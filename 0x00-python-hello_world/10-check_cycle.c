#include "lists.h"

/**
 * check_cycle - checks for a cycle/loop in a linked list
 *
 * @list: linked list input
 *
 * Return: 0 if there's no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *t = list;
	listint_t *s = list;

	while (t != NULL && s != NULL && t->next != NULL)
	{
		t = t->next;
		s = s->next->next;
		if (t == s)
			return (1);
	}

	return (0);
}
