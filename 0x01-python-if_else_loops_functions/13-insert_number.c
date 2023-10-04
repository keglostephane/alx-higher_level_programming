#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a storted singly linked list
 *
 * @head: head of the singly linked list
 *
 * @number: number to insert in the singly linked list
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp, *new_node;

	if (!head)
		return (NULL);

	if (!*head)
		return (add_nodeint_end(head, number));

	new_node = malloc(sizeof(listint_t *));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	node = *head;

	if (number < node->n)
	{
		new_node->next = node;
		return (new_node);
	}

	while (node)
	{
		if (node && node->next)
		{
			if ((number > node->n && number < node->next->n) ||
			    (number == node->n))
			{
				tmp = node->next;
				node->next = new_node;
				new_node->next = tmp;
				return (new_node);
			}
		}
		else
			if (number > node->n)
				return (add_nodeint_end(head, number));
		node = node->next;
	}
	return (NULL);
}
