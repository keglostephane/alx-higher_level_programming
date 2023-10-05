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

	if (!head || !*head)
		return (add_nodeint_end(head, number));

	new_node = malloc(sizeof(listint_t *));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	node = *head;

	while (node->next)
	{
		if (number < node->n && node == *head)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}

		if (number < node->next->n)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}

		node = node->next;
	}

	if (number > node->n)
	{
		node->next = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	return (NULL);

}
