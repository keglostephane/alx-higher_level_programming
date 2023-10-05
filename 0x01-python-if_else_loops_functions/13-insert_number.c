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
	listint_t *prev, *curr, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node || !head)
		return (NULL);

	new_node->n = number;

	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = *head;
	while (curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	prev->next = new_node;
	new_node->next = curr;

	return (new_node);
}
