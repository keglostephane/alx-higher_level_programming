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
	listint_t *prev, *curr, *node;

	node = malloc(sizeof(listint_t *));

	if (!node || !head)
		return (NULL);

	node->n = number;

	if (!*head || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	curr = *head;
	while (curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	prev->next = node;
	node->next = curr;

	return (node);
}
