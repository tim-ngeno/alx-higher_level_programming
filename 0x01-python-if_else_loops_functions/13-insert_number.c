#include "lists.h"

/**
 * insert_node - insert a number into a singly linked list
 *
 * @head: the head node
 * @number: the number to be inserted
 *
 * Return: On success, address of new node, Null otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *num;
	listint_t *temp = *head;

	num = malloc(sizeof(listint_t));
	if (num == NULL)
		return (NULL);
	num->n = number;
	num->next = NULL;

	if (*head)
	{
		while ((temp->next->n) <= (num->n))
		{
			temp = temp->next;
		}
		num->next = temp->next;
		temp->next = num;
	}

	return (num);
}
