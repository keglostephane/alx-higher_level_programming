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
	listint_t *node, *new_node;

	node = *head;

	if (!*head || number < node->n)
	{
		new_node = malloc(sizeof(listint_t *));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = node;
		*head = new_node;
		return (*head);
	}

	while (node)
	{
		if ((node->next && number < node->next->n) ||
		    (!node->next && number > node->n))
		{
			new_node = malloc(sizeof(listint_t *));
			if (!new_node)
				return (NULL);
			new_node->n = number;
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
	return (NULL);
}
