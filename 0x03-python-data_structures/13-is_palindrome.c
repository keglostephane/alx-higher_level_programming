#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - reverses a listint_t linked list
 *
 * @head: pointer to the head of the linked list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	prev = NULL;

	if (!*head)
		return (NULL);

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr, *curr2, *head2, *slow, *fast, *middle;

	if (!*head || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	/* Find the middle of the linked list */
	while (fast && fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* the location to use to split the list in half */
	middle = slow->next;

	head2 = NULL;
	/* reverse the second half of the list */
	head2 = reverse_listint(&middle);

	curr = *head;
	curr2 = head2;
	while (curr && curr2)
	{
		if (curr->n != curr2->n)
			break;
		curr = curr->next;
		curr2 = curr2->next;
	}
	/* restore the original state of the list */
	head2 = reverse_listint(&middle);

	if (!curr2)
		return (1);

	return (0);
}
