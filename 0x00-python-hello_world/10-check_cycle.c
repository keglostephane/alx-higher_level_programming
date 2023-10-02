#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 *
 * @list: head of the singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast, *head;

	head = list;
	slow = head, fast = head;

	do {
		slow = slow->next;
		if (fast && fast->next)
			fast = fast->next->next;
	} while (fast && fast != slow);

	if (!fast)
		return (0);

	return (1);
}
